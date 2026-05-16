"""CohereEmbedder tests — fully mocked, no network."""
from __future__ import annotations

import sys
from types import SimpleNamespace
from unittest.mock import MagicMock

import pytest

from verifiable_rag.embedders import CohereEmbedder, Embedder


@pytest.fixture
def fake_cohere(monkeypatch: pytest.MonkeyPatch) -> MagicMock:
    """Inject a fake ``cohere`` module with a stub ClientV2 that records calls."""
    fake_module = MagicMock(name="cohere_module")
    client = MagicMock(name="cohere_client")

    def _embed(*, texts, model, input_type, embedding_types):  # noqa: ANN001
        # Return a deterministic length-1024 vector per input (dim depends on model).
        dim = 384 if "light" in model else 1024
        vectors = [[float(i)] * dim for i in range(len(texts))]
        return SimpleNamespace(embeddings=SimpleNamespace(float_=vectors))

    client.embed.side_effect = _embed
    fake_module.ClientV2.return_value = client
    monkeypatch.setitem(sys.modules, "cohere", fake_module)
    return client


@pytest.mark.smoke
def test_satisfies_embedder_protocol(fake_cohere: MagicMock) -> None:
    assert isinstance(CohereEmbedder(api_key="x"), Embedder)


@pytest.mark.smoke
def test_dimension_matches_model(fake_cohere: MagicMock) -> None:
    assert CohereEmbedder(model="embed-english-v3.0", api_key="x").dimension == 1024
    assert CohereEmbedder(model="embed-english-light-v3.0", api_key="x").dimension == 384


@pytest.mark.smoke
def test_embed_uses_search_document_input_type(fake_cohere: MagicMock) -> None:
    e = CohereEmbedder(api_key="x")
    vecs = e.embed(["hello", "world"])
    assert len(vecs) == 2 and len(vecs[0]) == 1024
    call = fake_cohere.embed.call_args
    assert call.kwargs["input_type"] == "search_document"


@pytest.mark.smoke
def test_embed_query_uses_search_query_input_type(fake_cohere: MagicMock) -> None:
    e = CohereEmbedder(api_key="x")
    vec = e.embed_query("a question")
    assert len(vec) == 1024
    call = fake_cohere.embed.call_args
    assert call.kwargs["input_type"] == "search_query"


@pytest.mark.smoke
def test_embed_empty_list_is_noop(fake_cohere: MagicMock) -> None:
    e = CohereEmbedder(api_key="x")
    assert e.embed([]) == []
    fake_cohere.embed.assert_not_called()


@pytest.mark.smoke
def test_batching_splits_large_inputs(fake_cohere: MagicMock) -> None:
    """100 texts with batch_size=40 → 3 API calls."""
    e = CohereEmbedder(api_key="x", batch_size=40)
    vecs = e.embed(["t"] * 100)
    assert len(vecs) == 100
    assert fake_cohere.embed.call_count == 3


@pytest.mark.smoke
def test_missing_api_key_raises_at_use(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("COHERE_API_KEY", raising=False)
    e = CohereEmbedder(api_key=None)
    with pytest.raises(RuntimeError, match="COHERE_API_KEY"):
        e.embed(["x"])


@pytest.mark.smoke
def test_unknown_model_rejected() -> None:
    with pytest.raises(ValueError, match="Unknown Cohere embed model"):
        CohereEmbedder(model="embed-nonexistent-v99")


@pytest.mark.smoke
def test_batch_size_bounds_validated() -> None:
    with pytest.raises(ValueError, match="batch_size"):
        CohereEmbedder(batch_size=0, api_key="x")
    with pytest.raises(ValueError, match="batch_size"):
        CohereEmbedder(batch_size=200, api_key="x")  # > 96 Cohere limit
