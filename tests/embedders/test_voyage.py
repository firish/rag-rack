"""VoyageEmbedder tests.

All tests mock the voyageai client — no API key or network needed.
"""
from __future__ import annotations

from unittest.mock import MagicMock

import pytest

from verifiable_rag.embedders import Embedder, VoyageEmbedder

# --------------------------------------------------------------------------- #
# Fixtures
# --------------------------------------------------------------------------- #

def _make_voyage_response(n: int, dim: int) -> MagicMock:
    response = MagicMock()
    response.embeddings = [[float(i)] * dim for i in range(n)]
    return response


@pytest.fixture
def fake_voyage(monkeypatch: pytest.MonkeyPatch) -> MagicMock:
    """Patch voyageai.Client so no real API calls are made.

    voyageai is imported lazily inside _load(), so we inject a fake module
    into sys.modules before the lazy import fires.
    """
    import sys

    mock_client = MagicMock()
    mock_client.embed.side_effect = lambda texts, model, input_type: (
        _make_voyage_response(len(texts), 1024)
    )
    fake_module = MagicMock()
    fake_module.Client.return_value = mock_client
    monkeypatch.setitem(sys.modules, "voyageai", fake_module)
    return mock_client


# --------------------------------------------------------------------------- #
# Protocol conformance and construction
# --------------------------------------------------------------------------- #

@pytest.mark.smoke
def test_satisfies_embedder_protocol() -> None:
    embedder = VoyageEmbedder()
    assert isinstance(embedder, Embedder)


@pytest.mark.smoke
def test_unknown_model_raises() -> None:
    with pytest.raises(ValueError, match="Unknown Voyage model"):
        VoyageEmbedder(model="voyage-999-fake")


@pytest.mark.smoke
def test_batch_size_out_of_range_raises() -> None:
    with pytest.raises(ValueError, match="batch_size"):
        VoyageEmbedder(batch_size=0)
    with pytest.raises(ValueError, match="batch_size"):
        VoyageEmbedder(batch_size=129)


# --------------------------------------------------------------------------- #
# Dimension
# --------------------------------------------------------------------------- #

@pytest.mark.smoke
def test_dimension_voyage3() -> None:
    assert VoyageEmbedder(model="voyage-3").dimension == 1024


@pytest.mark.smoke
def test_dimension_voyage3_large() -> None:
    assert VoyageEmbedder(model="voyage-3-large").dimension == 1024


@pytest.mark.smoke
def test_dimension_voyage3_lite() -> None:
    assert VoyageEmbedder(model="voyage-3-lite").dimension == 512


# --------------------------------------------------------------------------- #
# embed() — document batching
# --------------------------------------------------------------------------- #

@pytest.mark.smoke
def test_embed_returns_one_vector_per_text(fake_voyage: MagicMock) -> None:
    embedder = VoyageEmbedder()
    results = embedder.embed(["Doc one.", "Doc two.", "Doc three."])
    assert len(results) == 3
    assert all(len(v) == 1024 for v in results)


@pytest.mark.smoke
def test_embed_empty_list_returns_empty(fake_voyage: MagicMock) -> None:
    embedder = VoyageEmbedder()
    assert embedder.embed([]) == []
    fake_voyage.embed.assert_not_called()


@pytest.mark.smoke
def test_embed_uses_document_input_type(fake_voyage: MagicMock) -> None:
    embedder = VoyageEmbedder()
    embedder.embed(["Some passage."])
    call_kwargs = fake_voyage.embed.call_args.kwargs
    assert call_kwargs["input_type"] == "document"


@pytest.mark.smoke
def test_embed_batches_large_inputs(monkeypatch: pytest.MonkeyPatch) -> None:
    """Inputs exceeding batch_size must be split into multiple API calls."""
    import sys

    call_count = 0

    def fake_embed(texts: list[str], **_kw: object) -> MagicMock:
        nonlocal call_count
        call_count += 1
        return _make_voyage_response(len(texts), 1024)

    mock_client = MagicMock()
    mock_client.embed.side_effect = fake_embed
    fake_module = MagicMock()
    fake_module.Client.return_value = mock_client
    monkeypatch.setitem(sys.modules, "voyageai", fake_module)

    embedder = VoyageEmbedder(batch_size=3)
    results = embedder.embed(["t"] * 7)  # 7 texts, batch=3 → 3 calls

    assert len(results) == 7
    assert call_count == 3


# --------------------------------------------------------------------------- #
# embed_query() — query input type
# --------------------------------------------------------------------------- #

@pytest.mark.smoke
def test_embed_query_returns_single_vector(fake_voyage: MagicMock) -> None:
    embedder = VoyageEmbedder()
    result = embedder.embed_query("What is attention?")
    assert len(result) == 1024


@pytest.mark.smoke
def test_embed_query_uses_query_input_type(fake_voyage: MagicMock) -> None:
    embedder = VoyageEmbedder()
    embedder.embed_query("test query")
    call_kwargs = fake_voyage.embed.call_args.kwargs
    assert call_kwargs["input_type"] == "query"
