from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from verifiable_rag.models.span import Span


@dataclass(frozen=True)
class Chunk:
    """Retrieval unit.

    Chunks carry the sentence_ids of every source sentence they contain so
    the citation layer can map retrieved chunks back to exact spans. This is
    the mechanism that decouples chunking granularity from citation granularity.
    """

    chunk_id: str
    text: str
    doc_id: str
    sentence_ids: tuple[str, ...]  # ordered, immutable
    span: Span                     # bounding span; may cross page boundaries
    metadata: dict[str, Any] = field(default_factory=dict, compare=False, hash=False)

    def __post_init__(self) -> None:
        if not self.sentence_ids:
            raise ValueError(f"Chunk {self.chunk_id!r} must reference at least one sentence")
        if self.span.doc_id != self.doc_id:
            raise ValueError(
                f"Chunk {self.chunk_id!r}: span.doc_id {self.span.doc_id!r} "
                f"!= doc_id {self.doc_id!r}"
            )


@dataclass(frozen=True)
class RetrievedChunk:
    """A chunk returned from the index with its retrieval score."""

    chunk: Chunk
    score: float
    retrieval_method: str  # "bm25" | "dense" | "hybrid"
