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
