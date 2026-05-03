from __future__ import annotations

from typing import Protocol, runtime_checkable


@runtime_checkable
class Embedder(Protocol):
    """Dense embedding interface.  Implementations must be deterministic."""

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
