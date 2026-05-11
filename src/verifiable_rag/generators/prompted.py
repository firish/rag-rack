"""PromptedCitedGenerator: baseline cited generator backed by LiteLLM.

Strategy
--------
Format the retrieved chunks as a list of *sentences*, each tagged with its
``sentence_id``.  Instruct the LLM to write its answer as discrete sentences,
each followed by bracketed sentence IDs that support the claim.  Parse the
output back into ``CitedSentence`` instances.

This is the **prompted** baseline mode (see ``GeneratorMode``).  It makes no
attempt to enforce citation structure via constrained decoding (Phase 3) or
post-hoc alignment (also Phase 3).  Citations rely entirely on the model
following instructions, so failure modes include:

* The model invents IDs not in the source set → we drop them and lower the
  confidence of that sentence to 0.
* The model writes a sentence with no bracket → confidence 0; the verifier
  and abstention layer decide whether to flag or strip.
* The model refuses (says "I cannot answer...") → we return an empty list,
  which Pipeline turns into a refusal.

LiteLLM gives us a single call shape for Anthropic, OpenAI, local models, etc.
"""

from __future__ import annotations

import re
from typing import Any

from verifiable_rag.generators import GeneratorMode
from verifiable_rag.models.answer import CitedSentence
from verifiable_rag.models.chunk import RetrievedChunk
from verifiable_rag.models.document import Document

# Matches any "[...]" group in the LLM output and captures the inside.
# Citation IDs use ``::`` plus word chars, e.g. ``mydoc-abc12345::s7``.  We
# don't constrain the inside here — invalid IDs are filtered later.
_BRACKET_RE = re.compile(r"\[([^\[\]]*)\]")
_ID_SPLIT_RE = re.compile(r"\s*,\s*")
_SENTENCE_SPLIT_RE = re.compile(r"(?<=[.!?])\s+")

# Heuristic refusal patterns the model may emit.  Kept short and exact to
# avoid stripping legitimate hedged answers.
_REFUSAL_PATTERNS = (
    "i cannot answer",
    "i can't answer",
    "i do not have enough information",
    "i don't have enough information",
    "the sources do not contain",
    "the provided sources do not",
)

_DEFAULT_SYSTEM_PROMPT = (
    "You are a careful research assistant. You answer questions strictly from "
    "the provided source sentences. You cite every claim with the sentence "
    "ID(s) it comes from. If the sources do not support a claim, do not make "
    "the claim. If you cannot answer at all from the sources, say so."
)

_USER_PROMPT_TEMPLATE = """\
Question: {query}

Sources (each line is one source sentence prefixed by its citation ID):
{sources}

Instructions:
1. Write the answer as one or more discrete sentences.
2. After EACH sentence, cite the supporting source IDs in brackets, e.g.:
   "Mitochondria produce ATP. [doc1::s5, doc1::s7]"
3. Use ONLY the source IDs shown above. Do not invent IDs.
4. If the sources do not answer the question, reply exactly:
   "I cannot answer this from the provided sources."

Answer:"""


class PromptedCitedGenerator:
    """Baseline cited generator using prompt instructions + LiteLLM.

    Parameters
    ----------
    model:
        LiteLLM model identifier, e.g. ``"claude-haiku-4-5-20251001"`` or
        ``"openai/gpt-4o-mini"``.  See LiteLLM docs for the full list.
    temperature:
        Sampling temperature.  Default 0 for deterministic citations.
    max_tokens:
        Hard cap on generated tokens.  Defaults to 1024.
    system_prompt:
        Override the default system prompt.
    api_base:
        Override LiteLLM's default API base (e.g. for local models).
    """

    mode: GeneratorMode = "prompted"

    def __init__(
        self,
        model: str = "claude-haiku-4-5-20251001",
        temperature: float = 0.0,
        max_tokens: int = 1024,
        system_prompt: str | None = None,
        api_base: str | None = None,
        num_retries: int = 3,
    ) -> None:
        if not (0.0 <= temperature <= 2.0):
            raise ValueError(f"temperature must be in [0, 2], got {temperature}")
        if max_tokens < 1:
            raise ValueError(f"max_tokens must be positive, got {max_tokens}")
        if num_retries < 0:
            raise ValueError(f"num_retries must be >= 0, got {num_retries}")

        self._model = model
        self._temperature = temperature
        self._max_tokens = max_tokens
        self._system_prompt = system_prompt or _DEFAULT_SYSTEM_PROMPT
        self._api_base = api_base
        self._num_retries = num_retries

    # ------------------------------------------------------------------ #
    # Generator Protocol
    # ------------------------------------------------------------------ #

    def generate(
        self,
        query: str,
        chunks: list[RetrievedChunk],
        documents: dict[str, Document],
    ) -> list[CitedSentence]:
        """Call the LLM and parse its cited output."""
        if not chunks:
            return []

        source_lines, valid_ids = self._format_sources(chunks, documents)
        if not source_lines:
            # No retrievable sentence text — generator cannot ground anything.
            return []

        user_prompt = _USER_PROMPT_TEMPLATE.format(
            query=query.strip(),
            sources="\n".join(source_lines),
        )

        raw = self._call_llm(user_prompt)
        if self._looks_like_refusal(raw):
            return []

        return self._parse_output(raw, valid_ids)

    # ------------------------------------------------------------------ #
    # Internals
    # ------------------------------------------------------------------ #

    def _format_sources(
        self,
        chunks: list[RetrievedChunk],
        documents: dict[str, Document],
    ) -> tuple[list[str], set[str]]:
        """Return (formatted source lines, set of valid sentence IDs)."""
        seen: set[str] = set()
        lines: list[str] = []

        for rc in chunks:
            doc = documents.get(rc.chunk.doc_id)
            if doc is None:
                # Pipeline didn't supply this document; fall back to chunk text
                # as a single anonymous source line keyed by chunk_id.
                if rc.chunk.chunk_id not in seen:
                    seen.add(rc.chunk.chunk_id)
                    lines.append(f"[{rc.chunk.chunk_id}] {rc.chunk.text}")
                continue

            for sid in rc.chunk.sentence_ids:
                if sid in seen:
                    continue
                try:
                    sentence = doc.sentence_by_id(sid)
                except KeyError:
                    # Sentence id pointed at a document we have, but the
                    # sentence is missing — silently skip so the LLM never
                    # sees an ID it can't trust.
                    continue
                seen.add(sid)
                lines.append(f"[{sid}] {sentence.text}")

        return lines, seen

    def _call_llm(self, user_prompt: str) -> str:
        """Invoke LiteLLM and return the assistant message string."""
        try:
            import litellm
        except ImportError as exc:
            raise ImportError(
                "litellm is required for PromptedCitedGenerator. "
                "Install with: pip install 'verifiable-rag[litellm]'"
            ) from exc

        kwargs: dict[str, Any] = {
            "model": self._model,
            "messages": [
                {"role": "system", "content": self._system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            "temperature": self._temperature,
            "max_tokens": self._max_tokens,
            # LiteLLM honors provider Retry-After headers and uses exponential
            # backoff on transient errors (rate limits, 5xx).
            "num_retries": self._num_retries,
        }
        if self._api_base is not None:
            kwargs["api_base"] = self._api_base

        response = litellm.completion(**kwargs)
        # LiteLLM returns an OpenAI-shaped response object.
        return str(response.choices[0].message.content or "").strip()

    @staticmethod
    def _looks_like_refusal(text: str) -> bool:
        lowered = text.lower()
        return any(p in lowered for p in _REFUSAL_PATTERNS)

    def _parse_output(
        self,
        raw: str,
        valid_ids: set[str],
    ) -> list[CitedSentence]:
        """Convert the LLM's raw text into a list of CitedSentence.

        Strategy: walk the text looking for ``[...]`` groups.  All text from
        the previous bracket (or start) up to each new bracket is one cited
        sentence with that bracket's IDs.  Anything trailing the last bracket
        is split on sentence punctuation and emitted with no citation.
        """
        cited: list[CitedSentence] = []
        cursor = 0

        for match in _BRACKET_RE.finditer(raw):
            sentence_text = raw[cursor : match.start()].strip()
            cursor = match.end()
            if not sentence_text:
                continue

            id_blob = match.group(1).strip()
            raw_ids = [s for s in _ID_SPLIT_RE.split(id_blob) if s]
            kept_ids = tuple(s for s in raw_ids if s in valid_ids)

            cited.append(
                CitedSentence(
                    text=sentence_text,
                    supporting_sentence_ids=kept_ids,
                    confidence=1.0 if kept_ids else 0.0,
                )
            )

        trailing = raw[cursor:].strip()
        if trailing:
            for piece in _SENTENCE_SPLIT_RE.split(trailing):
                piece = piece.strip()
                if piece:
                    cited.append(
                        CitedSentence(
                            text=piece,
                            supporting_sentence_ids=(),
                            confidence=0.0,
                        )
                    )

        return cited
