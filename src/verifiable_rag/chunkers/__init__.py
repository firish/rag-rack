from __future__ import annotations

from typing import Protocol, runtime_checkable

from verifiable_rag.chunkers.parent_child import ParentChildChunker
from verifiable_rag.chunkers.parent_expander import ParentExpander
from verifiable_rag.models.chunk import Chunk
from verifiable_rag.models.document import Document


@runtime_checkable
class Chunker(Protocol):
    """Split a Document into retrieval-sized Chunks while preserving sentence_ids.

    Span preservation invariant: every Chunk must list the sentence_ids of every
    Sentence it contains. Chunking granularity and citation granularity are
    decoupled — do not collapse sentence IDs into chunk IDs.
    """

    def chunk(self, document: Document) -> list[Chunk]:
        """Return chunks for all sentences in *document*."""
        ...


__all__ = ["Chunk", "Chunker", "ParentChildChunker", "ParentExpander"]
