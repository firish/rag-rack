"""VoyageEmbedder: wraps the Voyage AI API for production-grade embeddings.

Voyage-3 is the current retrieval SOTA (~73 MTEB).  Use it when eval numbers
matter more than cost.

Models and dimensions
---------------------
  voyage-3         1024-dim   Balanced quality/cost, recommended default
  voyage-3-large   1024-dim   Highest quality, ~2× cost of voyage-3
  voyage-3-lite     512-dim   Lowest cost, fast, good for high-volume indexing

Authentication
--------------
Pass ``api_key`` directly, or set the ``VOYAGE_API_KEY`` environment variable.
The voyageai client picks up the env var automatically when api_key is None.

Batching
--------
Voyage's API accepts up to 128 texts or ~320 K total tokens per request.
``embed()`` splits larger lists automatically — no manual batching needed.
"""
from __future__ import annotations

import os
from typing import Any

_VOYAGE_DIMENSIONS: dict[str, int] = {
    "voyage-3": 1024,
    "voyage-3-large": 1024,
    "voyage-3-lite": 512,
}
_VOYAGE_BATCH_LIMIT = 128


class VoyageEmbedder:
    """Production-grade embedder backed by Voyage AI's API.

    Parameters
    ----------
    model:
        Voyage model ID.  Defaults to ``"voyage-3"`` (balanced quality/cost).
    api_key:
        Voyage API key.  Falls back to the ``VOYAGE_API_KEY`` env var.
    batch_size:
        Max texts per API call.  Capped at 128 (Voyage's limit).
    """

    def __init__(
        self,
        model: str = "voyage-3",
        api_key: str | None = None,
        batch_size: int = 128,
    ) -> None:
        if model not in _VOYAGE_DIMENSIONS:
            raise ValueError(
                f"Unknown Voyage model {model!r}. "
                f"Known models: {sorted(_VOYAGE_DIMENSIONS)}"
            )
        if batch_size < 1 or batch_size > _VOYAGE_BATCH_LIMIT:
            raise ValueError(
                f"batch_size must be 1–{_VOYAGE_BATCH_LIMIT}, got {batch_size}"
            )
        self._model = model
        self._api_key = api_key or os.environ.get("VOYAGE_API_KEY")
        self._batch_size = batch_size
        self._client: Any = None  # voyageai.Client — lazy

    # ------------------------------------------------------------------ #
    # Embedder Protocol
    # ------------------------------------------------------------------ #

    @property
    def dimension(self) -> int:
        return _VOYAGE_DIMENSIONS[self._model]

    def embed(self, texts: list[str]) -> list[list[float]]:
        """Embed a batch of document/passage strings."""
        if not texts:
            return []
        return self._call(texts, input_type="document")

    def embed_query(self, query: str) -> list[float]:
        """Embed a single query string (uses Voyage's 'query' input_type)."""
        return self._call([query], input_type="query")[0]

    # ------------------------------------------------------------------ #
    # Internals
    # ------------------------------------------------------------------ #

    def _load(self) -> Any:
        if self._client is None:
            try:
                import voyageai
            except ImportError as exc:
                raise ImportError(
                    "voyageai is required for VoyageEmbedder. "
                    "Install with: pip install 'verifiable-rag[voyage]'"
                ) from exc
            self._client = voyageai.Client(api_key=self._api_key)
        return self._client

    def _call(self, texts: list[str], *, input_type: str) -> list[list[float]]:
        client = self._load()
        results: list[list[float]] = []
        for i in range(0, len(texts), self._batch_size):
            batch = texts[i : i + self._batch_size]
            response = client.embed(batch, model=self._model, input_type=input_type)
            results.extend(response.embeddings)
        return results

    def __repr__(self) -> str:
        return f"VoyageEmbedder(model={self._model!r}, dim={self.dimension})"
