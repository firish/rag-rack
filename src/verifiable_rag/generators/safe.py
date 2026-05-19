"""SAFECitedGenerator: SAFE-style atomic-claim-cited generator via structured outputs.

Strategy
--------
Extension of the ReClaim-style ``ConstrainedCitedGenerator`` that adds an
**atomic-claim decomposition layer** between sentences and citations. Each
generated sentence is broken into one or more atomic factual claims, and
citations attach to claims (not to the whole sentence).

Per-call JSON schema:

    {
      "refused": bool,
      "selected_option": str,
      "sentences": [
        {
          "text": "Full sentence in the answer.",
          "atomic_claims": [
            {"claim": "atomic fact 1", "citations": ["doc::s5"]},
            {"claim": "atomic fact 2", "citations": ["doc::s7", "doc::s9"]}
          ]
        }
      ]
    }

The atomic-claim layer is generated in the **same single LLM call** as the
sentences — single-pass, not the two-pass "generate-then-decompose" of the
original SAFE eval paper. This is closer to in-generation attribution
(SAFE May 2025 / "Ground every sentence") than post-hoc decomposition.

Compatibility with existing eval harness
----------------------------------------
The parser **flattens** atomic_claims back into our existing
``CitedSentence`` shape:

  * ``CitedSentence.text`` = the full sentence text
  * ``CitedSentence.supporting_sentence_ids`` = union of all atomic_claims'
    cites for that sentence
  * Loses per-atomic granularity for now — keeps every existing metric
    (citation_precision/recall/coverage, LLM-judge, etc.) working unchanged

The richer "per-atomic-claim cite trace" is available in the raw JSON
payload if downstream code wants to opt into atomic-level evaluation
(e.g., RAGTruth/FaithBench's atomic-claim-gold benchmarks). A future
version may extend ``CitedSentence`` itself with an atomic_claims field.

When does this help?
--------------------
* **RAGTruth / FaithBench** — gold is atomic-claim-level hallucination
  spans. Single-cite-per-sentence misses partial-claim failures; SAFE's
  atomic granularity catches them.
* **Compound scientific claims** — "X did A in 2020 and B in 2021" has
  two atomic facts that may have different cites.
* **Verifier integration** — NLI scoring per atomic claim is more
  precise than per-sentence (entailment of a sentence depends on its
  weakest claim).

When does it NOT help?
----------------------
* **LitQA2, ALCE** — sentence-level gold annotations. The flattened
  output is essentially identical to constrained mode there; atomic
  granularity is invisible to the metrics.

Refusal: same as constrained — ``{"refused": true, "sentences": []}``.
"""

from __future__ import annotations

import json
from typing import Any

from verifiable_rag.generators import GeneratorMode
from verifiable_rag.models.answer import CitedSentence
from verifiable_rag.models.chunk import RetrievedChunk
from verifiable_rag.models.document import Document

# Soft cap on citations per atomic claim. Atomic claims are smaller than
# sentences, so typically support comes from 1-2 sources. We allow up to 3
# but expect most claims to have 1-2.
_DEFAULT_MAX_CITATIONS_PER_CLAIM = 3
# Soft cap on atomic claims per sentence. Most sentences decompose into 1-3
# atomic claims; very long compound sentences may have up to 5. Hard-capping
# avoids degenerate over-decomposition.
_DEFAULT_MAX_CLAIMS_PER_SENTENCE = 5

_DEFAULT_SYSTEM_PROMPT = (
    "You are a careful research assistant. You answer questions strictly from "
    "the provided source sentences. When answer options are given, select the "
    "option best supported by the sources — you do not need a verbatim match; "
    "scientific inference and numeric approximation are acceptable. "
    "When the sources describe closely related conditions, related entities, "
    "or methodologies that differ only in non-material details, treat them as "
    "supporting evidence unless the difference is clearly central to the question. "
    "Decompose each answer sentence into its atomic factual claims (one fact per "
    "claim). For each atomic claim, cite the source sentence IDs that DIRECTLY "
    "support that specific claim. Prefer the smallest set of citations per "
    "atomic claim — usually 1, occasionally 2-3 when the claim genuinely "
    "combines facts. "
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
  - sentences: list of (text, atomic_claims) pairs. Each sentence's
    text should read naturally; its atomic_claims list breaks the
    sentence into individual factual assertions, each with its own
    citation set drawn from the sources above. Cite only valid IDs.
  - refused: set to true ONLY when the sources contain NO relevant
    information at all. If there is partial or indirect evidence, use
    it to select the best-supported option and set refused=false.
    When refused=true, set selected_option="Insufficient information
    to answer" and leave sentences empty."""


class SAFECitedGenerator:
    """SAFE-style atomic-claim cited generator using LiteLLM structured outputs.

    Functionally equivalent to :class:`ConstrainedCitedGenerator` with one
    architectural addition: each sentence is decomposed into atomic claims,
    and citations attach to atomic claims rather than whole sentences. This
    enables fine-grained verification on benchmarks with atomic-claim-level
    gold (RAGTruth, FaithBench).

    For benchmarks with sentence-level gold (LitQA2, ALCE), the parser
    flattens atomic_claims back into our existing ``CitedSentence`` shape
    so existing eval metrics work unchanged.

    Parameters
    ----------
    model:
        LiteLLM model identifier. Must support ``response_format``
        json_schema (Anthropic Sonnet/Haiku, OpenAI GPT-4o family, etc.).
    temperature:
        Sampling temperature.  Default 0 for deterministic citations.
    max_tokens:
        Hard cap on generated tokens.  Defaults to 4096 — atomic
        decomposition is more verbose than flat constrained output.
    system_prompt:
        Override the default system prompt.
    api_base:
        Override LiteLLM's default API base (e.g. for local models).
    num_retries:
        LiteLLM-level retry count for transient errors.
    max_citations_per_claim:
        Schema-enforced cap on citations per atomic claim. Default 3.
    max_claims_per_sentence:
        Schema-enforced cap on atomic claims per output sentence.
        Default 5.
    """

    mode: GeneratorMode = "safe"

    def __init__(
        self,
        model: str = "anthropic/claude-haiku-4-5",
        temperature: float = 0.0,
        max_tokens: int = 4096,
        system_prompt: str | None = None,
        api_base: str | None = None,
        num_retries: int = 3,
        max_citations_per_claim: int = _DEFAULT_MAX_CITATIONS_PER_CLAIM,
        max_claims_per_sentence: int = _DEFAULT_MAX_CLAIMS_PER_SENTENCE,
    ) -> None:
        if not (0.0 <= temperature <= 2.0):
            raise ValueError(f"temperature must be in [0, 2], got {temperature}")
        if max_tokens < 1:
            raise ValueError(f"max_tokens must be positive, got {max_tokens}")
        if num_retries < 0:
            raise ValueError(f"num_retries must be >= 0, got {num_retries}")
        if max_citations_per_claim < 1:
            raise ValueError(
                f"max_citations_per_claim must be >= 1, got {max_citations_per_claim}"
            )
        if max_claims_per_sentence < 1:
            raise ValueError(
                f"max_claims_per_sentence must be >= 1, got {max_claims_per_sentence}"
            )

        self._model = model
        self._temperature = temperature
        self._max_tokens = max_tokens
        self._system_prompt = system_prompt or _DEFAULT_SYSTEM_PROMPT
        self._api_base = api_base
        self._num_retries = num_retries
        self._max_cites = max_citations_per_claim
        self._max_claims = max_claims_per_sentence

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
        """Build per-call JSON schema with nested atomic_claims."""
        return {
            "name": "atomic_cited_answer",
            "strict": True,
            "schema": {
                "type": "object",
                "additionalProperties": False,
                "properties": {
                    "refused": {
                        "type": "boolean",
                        "description": (
                            "True iff the sources do not contain the answer."
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
                                    "description": "Full natural-language sentence.",
                                },
                                "atomic_claims": {
                                    "type": "array",
                                    "items": {
                                        "type": "object",
                                        "additionalProperties": False,
                                        "properties": {
                                            "claim": {
                                                "type": "string",
                                                "description": (
                                                    "One atomic factual "
                                                    "assertion drawn from "
                                                    "the sentence."
                                                ),
                                            },
                                            "citations": {
                                                "type": "array",
                                                "items": {
                                                    "type": "string",
                                                    "enum": valid_ids,
                                                },
                                                "minItems": 1,
                                                "maxItems": self._max_cites,
                                                "description": (
                                                    "Source sentence IDs that "
                                                    "DIRECTLY support this "
                                                    "atomic claim."
                                                ),
                                            },
                                        },
                                        "required": ["claim", "citations"],
                                    },
                                    "minItems": 1,
                                    "maxItems": self._max_claims,
                                },
                            },
                            "required": ["text", "atomic_claims"],
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
                "litellm is required for SAFECitedGenerator. "
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
    # Parsing — flatten atomic_claims into the existing CitedSentence shape
    # ------------------------------------------------------------------ #

    def _parse_output(self, raw: str, valid_ids: set[str]) -> list[CitedSentence]:
        """Convert the structured atomic-claim JSON into a flat list of
        CitedSentence — one per output sentence, with union-of-claim-cites
        as ``supporting_sentence_ids``.

        Defensive against:
          * malformed JSON (provider hiccup)
          * invalid citations that slipped past the enum
          * ``refused=true`` → empty list
        """
        try:
            payload = json.loads(raw)
        except json.JSONDecodeError:
            return []

        if not isinstance(payload, dict):
            return []
        if payload.get("refused"):
            return []

        cited: list[CitedSentence] = []

        # Prepend the bolded headline answer so MC matchers see it via tier-1
        # bold extraction (same trick as ConstrainedCitedGenerator).
        selected_option = str(payload.get("selected_option") or "").strip()
        if selected_option:
            cited.append(
                CitedSentence(
                    text=f"**{selected_option}**",
                    supporting_sentence_ids=(),
                    confidence=0.0,
                )
            )

        sentences_raw = payload.get("sentences") or []
        if not isinstance(sentences_raw, list):
            return cited  # only headline; no sentences

        for sentence_item in sentences_raw:
            if not isinstance(sentence_item, dict):
                continue
            text = str(sentence_item.get("text") or "").strip()
            if not text:
                continue
            atomic_claims = sentence_item.get("atomic_claims") or []
            if not isinstance(atomic_claims, list):
                continue
            union_cites: list[str] = []
            seen: set[str] = set()
            for ac in atomic_claims:
                if not isinstance(ac, dict):
                    continue
                raw_cites = ac.get("citations") or []
                if not isinstance(raw_cites, list):
                    continue
                for c in raw_cites:
                    cid = str(c)
                    if cid in valid_ids and cid not in seen:
                        seen.add(cid)
                        union_cites.append(cid)
            cited.append(
                CitedSentence(
                    text=text,
                    supporting_sentence_ids=tuple(union_cites),
                    confidence=1.0 if union_cites else 0.0,
                )
            )
        return cited
