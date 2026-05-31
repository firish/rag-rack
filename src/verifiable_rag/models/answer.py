from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from verifiable_rag.models.chunk import RetrievedChunk
from verifiable_rag.models.span import Span

Strictness = Literal["loose", "balanced", "strict", "paranoid"]


@dataclass(frozen=True)
class CitedSentence:
    """One sentence of generated output, grounded in source sentence IDs.

    supporting_sentence_ids references Sentence.id values in the source Document.
    An empty tuple means no citations — the verifier treats this as unsupported;
    the abstention layer decides whether to flag or refuse.
    """

    text: str
    supporting_sentence_ids: tuple[str, ...]
    confidence: float  # [0, 1] — generator-side confidence before NLI verification

    def __post_init__(self) -> None:
        if not (0.0 <= self.confidence <= 1.0):
            raise ValueError(f"confidence must be in [0, 1], got {self.confidence}")


@dataclass(frozen=True)
class VerificationResult:
    """NLI-based faithfulness check for one CitedSentence."""

    cited_sentence_index: int  # index into Answer.sentences
    claim_text: str
    is_supported: bool
    nli_score: float           # [0, 1] — entailment probability
    supporting_span: Span | None = None  # tightest source span supporting the claim


@dataclass(frozen=True)
class FaithfulnessComponents:
    """Decomposed faithfulness signal — exposed for auditability."""

    retrieval_score: float
    nli_score: float
    generation_logprob: float | None = None  # None when using closed-API generators


@dataclass
class Answer:
    """The complete output of a pipeline.ask() call."""

    query: str
    sentences: list[CitedSentence]
    faithfulness_score: float  # scalar in [0, 1] combining all signals
    faithfulness_components: FaithfulnessComponents
    unsupported_claims: list[str]
    retrieved_chunks: list[RetrievedChunk]
    verification_results: list[VerificationResult]
    strictness: Strictness = "balanced"
    was_refused: bool = False
    refusal_reason: str | None = None

    def __post_init__(self) -> None:
        if not (0.0 <= self.faithfulness_score <= 1.0):
            raise ValueError(
                f"faithfulness_score must be in [0, 1], got {self.faithfulness_score}"
            )
        if self.was_refused and self.refusal_reason is None:
            raise ValueError("was_refused=True requires a refusal_reason")

    @property
    def text(self) -> str:
        return " ".join(s.text for s in self.sentences)

    @property
    def is_fully_supported(self) -> bool:
        return not self.unsupported_claims and not self.was_refused

    # ------------------------------------------------------------------ #
    # Convenience accessors over the verification audit trail
    # ------------------------------------------------------------------ #

    def verification_for(self, sentence_idx: int) -> "VerificationResult | None":
        """Return the :class:`VerificationResult` for *sentence_idx*, or None.

        Lets callers map a CitedSentence index back to its NLI check
        without manually walking ``verification_results``::

            for i, sent in enumerate(answer.sentences):
                vr = answer.verification_for(i)
                if vr and not vr.is_supported:
                    log.warning(f"unsupported: {sent.text!r}")
        """
        for vr in self.verification_results:
            if vr.cited_sentence_index == sentence_idx:
                return vr
        return None

    @property
    def supported_sentences(self) -> list["CitedSentence"]:
        """Sentences whose verification said is_supported (or had no verifier).

        A sentence with no matching VerificationResult counts as
        supported — verification didn't run, so we don't penalize it.
        Use ``answer.unsupported_sentences`` for the strict complement.
        """
        return [
            s for i, s in enumerate(self.sentences)
            if (vr := self.verification_for(i)) is None or vr.is_supported
        ]

    @property
    def unsupported_sentences(self) -> list["CitedSentence"]:
        """Sentences explicitly flagged is_supported=False by the verifier."""
        return [
            s for i, s in enumerate(self.sentences)
            if (vr := self.verification_for(i)) is not None and not vr.is_supported
        ]

    @property
    def cited_sentence_ids(self) -> frozenset[str]:
        """Union of every source ``sentence_id`` cited across all sentences.

        Useful for "which sentences from the corpus did this answer pull
        from?" — without re-walking ``answer.sentences``.
        """
        out: set[str] = set()
        for s in self.sentences:
            out.update(s.supporting_sentence_ids)
        return frozenset(out)

    @property
    def nli_scores(self) -> list[float]:
        """Per-sentence NLI scores in ``verification_results`` order."""
        return [vr.nli_score for vr in self.verification_results]

    @property
    def min_nli_score(self) -> float:
        """The worst-case sentence-level NLI score.

        Returns 1.0 when no verifier ran — there's no evidence of
        unfaithfulness in the absence of a check.
        """
        scores = self.nli_scores
        return min(scores) if scores else 1.0

    def audit_trail(self) -> dict:
        """Structured audit trail as a JSON-serializable dict.

        Drop-in for observability stacks — emit this on every answer to
        track faithfulness over time, alert on unsupported claims, or
        slice metrics by upstream model. All fields are primitives.
        """
        fc = self.faithfulness_components
        nli = self.nli_scores
        return {
            "query": self.query,
            "strictness": self.strictness,
            "was_refused": self.was_refused,
            "refusal_reason": self.refusal_reason,
            # When verification_ran is False, faithfulness_score defaults
            # to 1.0 — there's no evidence of unfaithfulness, but no
            # evidence of faithfulness either. Distinct from "verifier
            # was configured on the Pipeline" — the Pipeline can have a
            # verifier attached yet skip verification (e.g. when the
            # generator produced no sentences to verify).
            "verification_ran": bool(self.verification_results),
            "faithfulness_score": self.faithfulness_score,
            "faithfulness_components": {
                "retrieval_score": fc.retrieval_score,
                "nli_score": fc.nli_score,
                "generation_logprob": fc.generation_logprob,
            },
            "n_sentences": len(self.sentences),
            "n_supported": len(self.supported_sentences),
            "n_unsupported": len(self.unsupported_sentences),
            "n_verified": len(self.verification_results),
            "min_nli_score": self.min_nli_score,
            "mean_nli_score": sum(nli) / len(nli) if nli else None,
            "unsupported_claims": list(self.unsupported_claims),
            "cited_sentence_ids": sorted(self.cited_sentence_ids),
            "n_retrieved_chunks": len(self.retrieved_chunks),
        }

    def to_html(self, title: str = "verifiable-rag report") -> str:
        """Render the full audit-trail HTML report for this Answer.

        Returns a self-contained HTML document string — inline CSS, no
        JavaScript, no external dependencies. Write it to a file and open
        in any browser::

            Path("report.html").write_text(answer.to_html())

        Shows the query, the answer with per-sentence verification color
        coding, the faithfulness components, the per-sentence NLI scores,
        and every reranked passage the generator saw. See
        :func:`verifiable_rag.report.to_html` for details.
        """
        from verifiable_rag.report import to_html

        return to_html(self, title=title)
