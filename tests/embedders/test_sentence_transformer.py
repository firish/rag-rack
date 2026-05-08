"""SentenceTransformerEmbedder tests.

Unit tests mock the sentence-transformers model so CI doesn't download
anything.  The ``@pytest.mark.slow`` integration test runs the real model
against BGE-small-en-v1.5 — run it locally to verify the real stack.
"""
from __future__ import annotations

from unittest.mock import MagicMock

import numpy as np
import pytest

from verifiable_rag.embedders import Embedder, SentenceTransformerEmbedder

# --------------------------------------------------------------------------- #
# Fixtures
# --------------------------------------------------------------------------- #

@pytest.fixture
def fake_st(monkeypatch: pytest.MonkeyPatch) -> MagicMock:
    """Patch SentenceTransformer so no model is downloaded.

    SentenceTransformer is imported lazily inside _load(), so it only exists
    inside a local import — monkeypatch.setattr can't reach it.  Instead we
    inject a fake module into sys.modules before the lazy import runs.
    """
    import sys

    mock_model = MagicMock()
    mock_model.get_sentence_embedding_dimension.return_value = 384
    mock_model.encode.side_effect = lambda texts, **_kw: np.ones(
        (len(texts), 384), dtype=np.float32
    )

    fake_module = MagicMock()
    fake_module.SentenceTransformer.return_value = mock_model
    monkeypatch.setitem(sys.modules, "sentence_transformers", fake_module)
    # Also reset any cached model on the embedder class so the fixture is fresh
    return mock_model


# --------------------------------------------------------------------------- #
# Protocol conformance
# --------------------------------------------------------------------------- #

@pytest.mark.smoke
def test_satisfies_embedder_protocol() -> None:
    embedder = SentenceTransformerEmbedder()
    assert isinstance(embedder, Embedder)


# --------------------------------------------------------------------------- #
# Lazy loading
# --------------------------------------------------------------------------- #

@pytest.mark.smoke
def test_construction_does_not_load_model(monkeypatch: pytest.MonkeyPatch) -> None:
    """Building the embedder must not trigger a model download."""
    import sys

    loaded: list[bool] = []

    mock_model = MagicMock()

    def fake_cls(*_a: object, **_kw: object) -> MagicMock:
        loaded.append(True)
        return mock_model

    fake_module = MagicMock()
    fake_module.SentenceTransformer.side_effect = fake_cls
    monkeypatch.setitem(sys.modules, "sentence_transformers", fake_module)

    SentenceTransformerEmbedder()  # must not call fake_cls
    assert not loaded


# --------------------------------------------------------------------------- #
# Dimension
# --------------------------------------------------------------------------- #

@pytest.mark.smoke
def test_dimension_returns_model_value(fake_st: MagicMock) -> None:
    embedder = SentenceTransformerEmbedder()
    assert embedder.dimension == 384


# --------------------------------------------------------------------------- #
# embed() — document/passage encoding
# --------------------------------------------------------------------------- #

@pytest.mark.smoke
def test_embed_returns_one_vector_per_text(fake_st: MagicMock) -> None:
    embedder = SentenceTransformerEmbedder()
    results = embedder.embed(["Hello world.", "Second sentence."])
    assert len(results) == 2
    assert all(len(v) == 384 for v in results)


@pytest.mark.smoke
def test_embed_empty_list_returns_empty(fake_st: MagicMock) -> None:
    embedder = SentenceTransformerEmbedder()
    assert embedder.embed([]) == []


@pytest.mark.smoke
def test_embed_passes_no_instruction_for_documents(fake_st: MagicMock) -> None:
    """Documents must be encoded as-is — no query instruction prefix."""
    embedder = SentenceTransformerEmbedder()
    embedder.embed(["My document text."])
    call_args = fake_st.encode.call_args
    encoded_texts = call_args[0][0]
    assert encoded_texts == ["My document text."]


# --------------------------------------------------------------------------- #
# embed_query() — query encoding with instruction prefix
# --------------------------------------------------------------------------- #

@pytest.mark.smoke
def test_embed_query_returns_single_vector(fake_st: MagicMock) -> None:
    embedder = SentenceTransformerEmbedder()
    result = embedder.embed_query("What is backpropagation?")
    assert len(result) == 384


@pytest.mark.smoke
def test_embed_query_prepends_bge_instruction(fake_st: MagicMock) -> None:
    """BGE-small must prepend its retrieval instruction to queries."""
    embedder = SentenceTransformerEmbedder(model_name="BAAI/bge-small-en-v1.5")
    embedder.embed_query("What is backpropagation?")
    call_args = fake_st.encode.call_args
    encoded_texts = call_args[0][0]
    assert encoded_texts[0].startswith(
        "Represent this sentence for searching relevant passages: "
    )
    assert "backpropagation" in encoded_texts[0]


@pytest.mark.smoke
def test_embed_query_no_instruction_for_m3(fake_st: MagicMock) -> None:
    """BGE-M3 uses no instruction — query is encoded verbatim."""
    fake_st.get_sentence_embedding_dimension.return_value = 1024
    fake_st.encode.side_effect = lambda texts, **_kw: np.ones(
        (len(texts), 1024), dtype=np.float32
    )
    embedder = SentenceTransformerEmbedder(model_name="BAAI/bge-m3")
    embedder.embed_query("What is backpropagation?")
    call_args = fake_st.encode.call_args
    encoded_texts = call_args[0][0]
    assert encoded_texts[0] == "What is backpropagation?"


@pytest.mark.smoke
def test_explicit_empty_instruction_disables_prefix(fake_st: MagicMock) -> None:
    """Passing query_instruction='' explicitly overrides the defaults table."""
    embedder = SentenceTransformerEmbedder(
        model_name="BAAI/bge-small-en-v1.5",
        query_instruction="",
    )
    embedder.embed_query("test query")
    call_args = fake_st.encode.call_args
    assert call_args[0][0][0] == "test query"


@pytest.mark.smoke
def test_custom_instruction_is_prepended(fake_st: MagicMock) -> None:
    embedder = SentenceTransformerEmbedder(
        model_name="some/custom-model",
        query_instruction="Query: ",
    )
    embedder.embed_query("hello")
    call_args = fake_st.encode.call_args
    assert call_args[0][0][0] == "Query: hello"


# --------------------------------------------------------------------------- #
# normalize flag
# --------------------------------------------------------------------------- #

@pytest.mark.smoke
def test_normalize_flag_passed_to_encode(fake_st: MagicMock) -> None:
    embedder = SentenceTransformerEmbedder(normalize=False)
    embedder.embed(["text"])
    call_kwargs = fake_st.encode.call_args.kwargs
    assert call_kwargs.get("normalize_embeddings") is False


# --------------------------------------------------------------------------- #
# Real model — only runs when sentence-transformers + network available
# --------------------------------------------------------------------------- #

@pytest.mark.slow
def test_real_bge_small_embed_and_query() -> None:
    pytest.importorskip("sentence_transformers")
    embedder = SentenceTransformerEmbedder(model_name="BAAI/bge-small-en-v1.5")

    assert embedder.dimension == 384

    vecs = embedder.embed(["The sky is blue.", "Neural networks learn representations."])
    assert len(vecs) == 2
    assert all(len(v) == 384 for v in vecs)

    # With normalize=True all vectors should be unit length
    import math
    for v in vecs:
        magnitude = math.sqrt(sum(x * x for x in v))
        assert abs(magnitude - 1.0) < 1e-4, f"Vector not unit length: {magnitude}"

    query_vec = embedder.embed_query("What color is the sky?")
    assert len(query_vec) == 384
    magnitude = math.sqrt(sum(x * x for x in query_vec))
    assert abs(magnitude - 1.0) < 1e-4
