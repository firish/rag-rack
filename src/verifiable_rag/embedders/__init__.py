from __future__ import annotations

from typing import Protocol, runtime_checkable

from verifiable_rag.embedders.sentence_transformer import SentenceTransformerEmbedder
from verifiable_rag.embedders.voyage import VoyageEmbedder


@runtime_checkable
class Embedder(Protocol):
    """Dense embedding interface.  Implementations must be deterministic.

    ``embed()`` is for documents/passages (indexing time).
    ``embed_query()`` is for query strings (search time) — some models apply
    a different instruction prefix for queries vs passages, which improves
    retrieval recall on asymmetric tasks.
    """

    @property
    def dimension(self) -> int:
        """Output embedding dimension."""
        ...

    def embed(self, texts: list[str]) -> list[list[float]]:
        """Return one embedding per text, in the same order."""
        ...

    def embed_query(self, query: str) -> list[float]:
        """Embed a single query string (may use a different prompt prefix)."""
        ...


__all__ = ["Embedder", "SentenceTransformerEmbedder", "VoyageEmbedder"]
