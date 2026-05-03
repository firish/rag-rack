from __future__ import annotations

from typing import Protocol, runtime_checkable

from verifiable_rag.models.chunk import Chunk, RetrievedChunk


@runtime_checkable
class DenseIndex(Protocol):
    """ANN vector index backed by LanceDB (default) or similar."""

    def add(self, chunks: list[Chunk], embeddings: list[list[float]]) -> None:
        """Index *chunks* with their pre-computed *embeddings*."""
        ...

    def search(self, query_embedding: list[float], k: int) -> list[RetrievedChunk]:
        """Return up to *k* chunks by approximate nearest-neighbour search."""
        ...


@runtime_checkable
class SparseIndex(Protocol):
    """BM25 or TF-IDF sparse retrieval index."""

    def add(self, chunks: list[Chunk]) -> None:
        ...

    def search(self, query: str, k: int) -> list[RetrievedChunk]:
        ...


@runtime_checkable
class HybridIndex(Protocol):
    """Combined dense + sparse index with RRF or weighted fusion."""

    def add(self, chunks: list[Chunk], embeddings: list[list[float]]) -> None:
        ...

    def search(
        self,
        query: str,
        query_embedding: list[float],
        k: int,
    ) -> list[RetrievedChunk]:
        ...
