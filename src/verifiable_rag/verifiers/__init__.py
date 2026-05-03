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
