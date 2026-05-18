from __future__ import annotations

from typing import Literal, Protocol, runtime_checkable

from verifiable_rag.models.answer import CitedSentence
from verifiable_rag.models.chunk import RetrievedChunk
from verifiable_rag.models.document import Document

GeneratorMode = Literal["prompted", "constrained", "post_hoc"]


@runtime_checkable
class Generator(Protocol):
    """Generates an answer grounded in retrieved chunks.

    Modes:
      prompted    — baseline: prompt instructs the LLM to cite by sentence ID.
      constrained — ReClaim-style: constrained decoding enforces citation structure.
      post_hoc    — two-pass: generate freely, then align output to source sentences.

    Output: one CitedSentence per output sentence. Each CitedSentence carries
    (text, supporting_sentence_ids, confidence). An empty supporting_sentence_ids
    means the generator could not ground the claim — do not silently return it.
    """

    mode: GeneratorMode

    def generate(
        self,
        query: str,
        chunks: list[RetrievedChunk],
        documents: dict[str, Document],
    ) -> list[CitedSentence]:
        """Generate cited sentences for *query* given *chunks* from *documents*."""
        ...


# Concrete implementations — imported after Protocol to avoid circular imports
from verifiable_rag.generators.constrained import ConstrainedCitedGenerator  # noqa: E402
from verifiable_rag.generators.prompted import PromptedCitedGenerator  # noqa: E402

__all__ = [
    "ConstrainedCitedGenerator",
    "Generator",
    "GeneratorMode",
    "PromptedCitedGenerator",
]
