from __future__ import annotations

from typing import Protocol, runtime_checkable

from verifiable_rag.models.answer import CitedSentence, VerificationResult
from verifiable_rag.models.document import Document


@runtime_checkable
class Verifier(Protocol):
    """Post-hoc faithfulness verifier.

    Decomposes each CitedSentence into atomic claims, checks each claim
    against its cited source span via NLI, and returns a VerificationResult
    per sentence.

    In strict/paranoid modes the Pipeline will refuse unsupported sentences.
    In loose mode the verifier may be skipped entirely.
    """

    def verify(
        self,
        sentences: list[CitedSentence],
        documents: dict[str, Document],
    ) -> list[VerificationResult]:
        """Return one VerificationResult per CitedSentence, in the same order."""
        ...


@runtime_checkable
class NLIScorer(Protocol):
    """Raw (premise, hypothesis) → entailment-probability scoring.

    A thinner interface than :class:`Verifier`. Used by verifier-only
    benchmarks (e.g. RAGTruth) that have pre-generated responses and just
    need the underlying NLI signal, not the CitedSentence/Document
    ceremony. Future verifiers (MiniCheck, DualNLI, LLM-judge) will all
    expose this too so the same runner scores them apples-to-apples.
    """

    def score_pairs(self, pairs: list[tuple[str, str]]) -> list[float]:
        """Score a batch of (premise, hypothesis) pairs.

        Returns one float in ``[0, 1]`` per pair (higher = more supported).
        """
        ...


# Concrete implementations — imported after Protocol to avoid circular imports
from verifiable_rag.verifiers.dual_nli import DualNLIVerifier  # noqa: E402
from verifiable_rag.verifiers.ensemble import EnsembleScorer  # noqa: E402
from verifiable_rag.verifiers.hhem import HHEMVerifier  # noqa: E402
from verifiable_rag.verifiers.llm_judge import LLMJudgeVerifier  # noqa: E402
from verifiable_rag.verifiers.minicheck import MiniCheckVerifier  # noqa: E402
from verifiable_rag.verifiers.modal_remote import (  # noqa: E402
    ModalHHEMScorer,
    ModalMiniCheckScorer,
)

__all__ = [
    "DualNLIVerifier",
    "EnsembleScorer",
    "HHEMVerifier",
    "LLMJudgeVerifier",
    "MiniCheckVerifier",
    "ModalHHEMScorer",
    "ModalMiniCheckScorer",
    "NLIScorer",
    "Verifier",
]
