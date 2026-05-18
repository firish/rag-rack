"""ConstrainedCitedGenerator: ReClaim-style cited generator via structured outputs.

Strategy
--------
Build a JSON schema per-call that constrains the LLM's output to:
  * a list of (text, citations[]) pairs
  * where each citation MUST come from an enum of valid sentence IDs
    drawn from the retrieved chunks
  * plus a top-level ``refused`` boolean for clean abstention

This eliminates the failure modes of the prompted baseline:
  * **invented IDs** — impossible because the enum constrains decoding
  * **decoration / wrong-doc cites** — same: every citation token is in-set
  * **format drift** — schema forces shape; no regex parsing of prose

Reference: ReClaim, "Ground Every Sentence" (ACL 2024). The key
operationalisation here is *closed-model structured outputs* — Anthropic
tool-use under the hood, OpenAI native structured outputs. Token-level
constrained decoding for open-weights models (outlines / lm-format-enforcer)
is a Phase 5 follow-on.

Multi-citation by default
-------------------------
Unlike the original ReClaim formulation (single citation per claim), we
allow ``minItems=1, maxItems=3`` citations per sentence. Real scientific
claims often draw from multiple sources; capping at one structurally
suppresses citation_recall. The ``maxItems`` cap discourages decoration
without hard-blocking legitimate triple-support cases.

Refusal
-------
Set ``{"refused": true, "sentences": []}`` when the sources do not
contain the answer. The generator returns an empty list (same as
PromptedCitedGenerator on refusal) so the Pipeline's downstream logic
is unchanged.
"""

from __future__ import annotations

import json
from typing import Any

from verifiable_rag.generators import GeneratorMode
from verifiable_rag.models.answer import CitedSentence
from verifiable_rag.models.chunk import RetrievedChunk
from verifiable_rag.models.document import Document

# Soft cap on citations per sentence. Set higher than ReClaim's single-cite
# baseline but tight enough to discourage decoration. Real scientific claims
# rarely combine more than 2-3 sources cleanly.
_DEFAULT_MAX_CITATIONS = 3

_DEFAULT_SYSTEM_PROMPT = (
    "You are a careful research assistant. You answer questions strictly from "
    "the provided source sentences. When answer options are given, select the "
    "option best supported by the sources — you do not need a verbatim match; "
    "scientific inference and numeric approximation are acceptable. "
    "When the sources describe closely related conditions, related entities, "
    "or methodologies that differ only in non-material details, treat them as "
    "supporting evidence unless the difference is clearly central to the question. "
    "Cite each claim with the source sentence IDs that DIRECTLY support it. "
    "Prefer the smallest set of citations that fully supports the claim. "
    "Only set refused=true when the sources contain NO relevant information at "
    "all. If the sources provide partial or indirect evidence, use that "
    "evidence to select the best-supported option."
)

_USER_PROMPT_TEMPLATE = """\
Question: {query}

Sources (each line is one source sentence prefixed by its citation ID):
{sources}

Fill in the structured response:
  - selected_option: the EXACT text of the answer option you picked from
    the question above (verbatim, copied from the options list). If the
    question is open-ended (no options listed), give a short headline
    answer.
  - sentences: explanation as a list of (text, citations) pairs. Cite
    only valid source IDs from the sources above.
  - refused: set to true ONLY when the sources contain NO relevant
    information at all. If there is partial or indirect evidence, use
    it to select the best-supported option and set refused=false.
    When refused=true, set selected_option="Insufficient information
    to answer" and leave sentences empty."""


class ConstrainedCitedGenerator:
    """Constrained-decoding cited generator using LiteLLM structured outputs.

    Parameters
    ----------
    model:
        LiteLLM model identifier. Must support ``response_format``
        json_schema (Anthropic Sonnet/Haiku, OpenAI GPT-4o family, etc.).
    temperature:
        Sampling temperature.  Default 0 for deterministic citations.
    max_tokens:
        Hard cap on generated tokens.  Defaults to 2048 (structured JSON
        is more verbose than free prose).
    system_prompt:
        Override the default system prompt.
    api_base:
        Override LiteLLM's default API base (e.g. for local models).
    num_retries:
        LiteLLM-level retry count for transient errors.
    max_citations_per_sentence:
        Schema-enforced cap on the citations array per output sentence.
        Default 3.
    """

    mode: GeneratorMode = "constrained"

    def __init__(
        self,
        model: str = "anthropic/claude-haiku-4-5",
        temperature: float = 0.0,
        max_tokens: int = 2048,
        system_prompt: str | None = None,
        api_base: str | None = None,
        num_retries: int = 3,
        max_citations_per_sentence: int = _DEFAULT_MAX_CITATIONS,
    ) -> None:
        if not (0.0 <= temperature <= 2.0):
            raise ValueError(f"temperature must be in [0, 2], got {temperature}")
        if max_tokens < 1:
            raise ValueError(f"max_tokens must be positive, got {max_tokens}")
        if num_retries < 0:
            raise ValueError(f"num_retries must be >= 0, got {num_retries}")
        if max_citations_per_sentence < 1:
            raise ValueError(
                f"max_citations_per_sentence must be >= 1, got {max_citations_per_sentence}"
            )

        self._model = model
        self._temperature = temperature
        self._max_tokens = max_tokens
        self._system_prompt = system_prompt or _DEFAULT_SYSTEM_PROMPT
        self._api_base = api_base
        self._num_retries = num_retries
        self._max_citations = max_citations_per_sentence

    # ------------------------------------------------------------------ #
    # Generator Protocol
    # ------------------------------------------------------------------ #

    def generate(
        self,
        query: str,
        chunks: list[RetrievedChunk],
        documents: dict[str, Document],
    ) -> list[CitedSentence]:
        if not chunks:
            return []

        source_lines, valid_ids = self._format_sources(chunks, documents)
        if not source_lines:
            return []

        schema = self._build_schema(sorted(valid_ids))

        user_prompt = _USER_PROMPT_TEMPLATE.format(
            query=query.strip(),
            sources="\n".join(source_lines),
        )

        raw = self._call_llm(user_prompt, schema)
        return self._parse_output(raw, valid_ids)

    # ------------------------------------------------------------------ #
    # Source formatting (mirrors PromptedCitedGenerator)
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
                    continue
                seen.add(sid)
                lines.append(f"[{sid}] {sentence.text}")

        return lines, seen

    # ------------------------------------------------------------------ #
    # Schema + LLM call
    # ------------------------------------------------------------------ #

    def _build_schema(self, valid_ids: list[str]) -> dict[str, Any]:
        """Build the per-call JSON schema with the citation enum populated."""
        return {
            "name": "cited_answer",
            "strict": True,
            "schema": {
                "type": "object",
                "additionalProperties": False,
                "properties": {
                    "refused": {
                        "type": "boolean",
                        "description": (
                            "True iff the sources do not contain the answer. "
                            "Set sentences to [] when true."
                        ),
                    },
                    "selected_option": {
                        "type": "string",
                        "description": (
                            "For multiple-choice questions: the EXACT text "
                            "of the chosen option (verbatim from the options "
                            "list). For open questions: a short headline "
                            "answer. When refused=true, set this to "
                            "'Insufficient information to answer'."
                        ),
                    },
                    "sentences": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "additionalProperties": False,
                            "properties": {
                                "text": {
                                    "type": "string",
                                    "description": "One answer sentence.",
                                },
                                "citations": {
                                    "type": "array",
                                    "items": {
                                        "type": "string",
                                        "enum": valid_ids,
                                    },
                                    "minItems": 1,
                                    "maxItems": self._max_citations,
                                    "description": (
                                        "Source sentence IDs that DIRECTLY "
                                        "support this sentence."
                                    ),
                                },
                            },
                            "required": ["text", "citations"],
                        },
                    },
                },
                "required": ["refused", "selected_option", "sentences"],
            },
        }

    def _call_llm(self, user_prompt: str, schema: dict[str, Any]) -> str:
        """Invoke LiteLLM with response_format=json_schema and return raw JSON."""
        try:
            import litellm
        except ImportError as exc:
            raise ImportError(
                "litellm is required for ConstrainedCitedGenerator. "
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
            "num_retries": self._num_retries,
            "response_format": {
                "type": "json_schema",
                "json_schema": schema,
            },
        }
        if self._api_base is not None:
            kwargs["api_base"] = self._api_base

        response = litellm.completion(**kwargs)
        return str(response.choices[0].message.content or "").strip()

    # ------------------------------------------------------------------ #
    # Parsing
    # ------------------------------------------------------------------ #

    def _parse_output(self, raw: str, valid_ids: set[str]) -> list[CitedSentence]:
        """Convert the structured JSON response into CitedSentence list.

        The schema *should* guarantee well-formed output, but we defend
        against:
          * malformed JSON (provider hiccup)
          * citations that snuck past the enum (very rare, but possible
            if a provider's enforcement is soft)
          * ``refused=true`` → empty sentences regardless of any text

        When ``selected_option`` is present and the response isn't a refusal,
        we prepend a synthesized bold headline sentence (no citation, zero
        confidence) so downstream MC matchers can read the model's pick
        without having to parse the explanatory prose. The bold headline
        is purely a parsing aid — it carries no citation weight.
        """
        try:
            payload = json.loads(raw)
        except json.JSONDecodeError:
            return []

        if not isinstance(payload, dict):
            return []
        if payload.get("refused"):
            return []

        sentences_raw = payload.get("sentences") or []
        if not isinstance(sentences_raw, list):
            return []

        cited: list[CitedSentence] = []

        # Prepend the bolded headline answer so MC matchers see it via
        # tier-1 bold extraction. No citation — this is a parsing aid,
        # not a substantive claim.
        selected_option = str(payload.get("selected_option") or "").strip()
        if selected_option:
            cited.append(
                CitedSentence(
                    text=f"**{selected_option}**",
                    supporting_sentence_ids=(),
                    confidence=0.0,
                )
            )

        for item in sentences_raw:
            if not isinstance(item, dict):
                continue
            text = str(item.get("text") or "").strip()
            if not text:
                continue
            raw_citations = item.get("citations") or []
            if not isinstance(raw_citations, list):
                continue
            # Defensive enum filter (no-op when provider enforces strictly).
            kept_ids = tuple(
                str(c) for c in raw_citations if str(c) in valid_ids
            )
            cited.append(
                CitedSentence(
                    text=text,
                    supporting_sentence_ids=kept_ids,
                    confidence=1.0 if kept_ids else 0.0,
                )
            )
        return cited
