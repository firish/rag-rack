from __future__ import annotations

from typing import Protocol, runtime_checkable

from verifiable_rag.models.chunk import RetrievedChunk


@runtime_checkable
class Reranker(Protocol):
    """Cross-encoder or listwise reranker.

    Receives top-K retrieved chunks and re-scores them with query context.
    Returns a shorter, better-ordered list for the generator.
    """

    def rerank(
        self,
        query: str,
        chunks: list[RetrievedChunk],
        top_k: int = 5,
    ) -> list[RetrievedChunk]:
        """Return at most *top_k* chunks in descending relevance order."""
        ...


# Concrete implementations — imported after Protocol to avoid circular imports
from verifiable_rag.rerankers.bge import BGERerankerV2  # noqa: E402
from verifiable_rag.rerankers.cohere_reranker import CohereReranker  # noqa: E402

__all__ = ["Reranker", "BGERerankerV2", "CohereReranker"]
