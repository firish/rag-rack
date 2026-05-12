"""BGERerankerV2 tests.

We patch sentence_transformers into sys.modules so no model is downloaded,
mirroring the SentenceTransformerEmbedder test pattern. The fake
CrossEncoder.predict returns a controllable score vector, so we can assert
on ordering without running real inference.
"""

from __future__ import annotations

import sys
from typing import Any
from unittest.mock import MagicMock

import numpy as np
import pytest

from verifiable_rag.models.chunk import Chunk, RetrievedChunk
from verifiable_rag.models.span import Span
from verifiable_rag.rerankers import BGERerankerV2, Reranker

# --------------------------------------------------------------------------- #
# Fixtures
# --------------------------------------------------------------------------- #


@pytest.fixture
def fake_st(monkeypatch: pytest.MonkeyPatch) -> MagicMock:
    """Inject a fake sentence_transformers module with a controllable CrossEncoder."""
    mock_model = MagicMock()
    # Default: identity-like scores (chunk i gets score i+1)
    mock_model.predict.side_effect = lambda pairs, **_kw: np.array(
        [float(i + 1) for i in range(len(pairs))]
    )

    fake_module = MagicMock()
    fake_module.CrossEncoder.return_value = mock_model
    monkeypatch.setitem(sys.modules, "sentence_transformers", fake_module)
    return mock_model


def _make_chunks(n: int) -> list[RetrievedChunk]:
    return [
        RetrievedChunk(
            chunk=Chunk(
                chunk_id=f"doc::ch{i}",
                text=f"chunk text {i}",
                doc_id="doc",
                sentence_ids=(f"doc::s{i}",),
                span=Span(doc_id="doc", char_start=i * 10, char_end=i * 10 + 9),
                metadata={"section_id": "doc::sec0", "paragraph_id": f"doc::p{i}"},
            ),
            score=0.5,
            retrieval_method="hybrid",
        )
        for i in range(n)
    ]


# --------------------------------------------------------------------------- #
# Protocol conformance
# --------------------------------------------------------------------------- #


@pytest.mark.smoke
def test_satisfies_reranker_protocol() -> None:
    rr = BGERerankerV2()
    assert isinstance(rr, Reranker)


@pytest.mark.smoke
def test_construction_does_not_load_model(monkeypatch: pytest.MonkeyPatch) -> None:
    """Construction must be cheap — no model download."""
    loaded: list[bool] = []

    def fake_cls(*_a: object, **_kw: object) -> MagicMock:
        loaded.append(True)
        return MagicMock()

    fake_module = MagicMock()
    fake_module.CrossEncoder.side_effect = fake_cls
    monkeypatch.setitem(sys.modules, "sentence_transformers", fake_module)

    BGERerankerV2()
    assert not loaded


# --------------------------------------------------------------------------- #
# Constructor validation
# --------------------------------------------------------------------------- #


@pytest.mark.smoke
def test_invalid_batch_size_raises() -> None:
    with pytest.raises(ValueError, match="batch_size"):
        BGERerankerV2(batch_size=0)


@pytest.mark.smoke
def test_invalid_max_length_raises() -> None:
    with pytest.raises(ValueError, match="max_length"):
        BGERerankerV2(max_length=0)


# --------------------------------------------------------------------------- #
# rerank() — edge cases
# --------------------------------------------------------------------------- #


@pytest.mark.smoke
def test_rerank_empty_chunks_returns_empty(fake_st: MagicMock) -> None:
    rr = BGERerankerV2()
    assert rr.rerank("query", [], top_k=5) == []
    fake_st.predict.assert_not_called()


@pytest.mark.smoke
def test_rerank_top_k_zero_returns_empty(fake_st: MagicMock) -> None:
    rr = BGERerankerV2()
    assert rr.rerank("query", _make_chunks(3), top_k=0) == []
    fake_st.predict.assert_not_called()


@pytest.mark.smoke
def test_rerank_top_k_larger_than_input_returns_all(fake_st: MagicMock) -> None:
    rr = BGERerankerV2()
    out = rr.rerank("q", _make_chunks(3), top_k=10)
    assert len(out) == 3


# --------------------------------------------------------------------------- #
# rerank() — ordering and scoring
# --------------------------------------------------------------------------- #


@pytest.mark.smoke
def test_rerank_orders_by_score_descending(fake_st: MagicMock) -> None:
    """Highest cross-encoder score should come first."""
    # Make chunk 1 the winner with a clear score gap
    fake_st.predict.side_effect = lambda pairs, **_kw: np.array([0.1, 0.9, 0.5])

    rr = BGERerankerV2()
    out = rr.rerank("q", _make_chunks(3), top_k=3)

    assert [r.chunk.chunk_id for r in out] == ["doc::ch1", "doc::ch2", "doc::ch0"]
    assert out[0].score == pytest.approx(0.9)
    assert out[1].score == pytest.approx(0.5)
    assert out[2].score == pytest.approx(0.1)


@pytest.mark.smoke
def test_rerank_truncates_to_top_k(fake_st: MagicMock) -> None:
    fake_st.predict.side_effect = lambda pairs, **_kw: np.array([0.1, 0.9, 0.5, 0.7, 0.3])
    rr = BGERerankerV2()
    out = rr.rerank("q", _make_chunks(5), top_k=2)

    assert len(out) == 2
    # Top 2 by score: 0.9 (ch1), 0.7 (ch3)
    assert [r.chunk.chunk_id for r in out] == ["doc::ch1", "doc::ch3"]


@pytest.mark.smoke
def test_rerank_replaces_score_and_method(fake_st: MagicMock) -> None:
    """Reranker scores replace RRF scores; retrieval_method becomes 'reranked'."""
    fake_st.predict.side_effect = lambda pairs, **_kw: np.array([0.42])
    rr = BGERerankerV2()
    out = rr.rerank("q", _make_chunks(1), top_k=1)

    assert out[0].score == pytest.approx(0.42)
    assert out[0].retrieval_method == "reranked"


# --------------------------------------------------------------------------- #
# rerank() — what's sent to the cross-encoder
# --------------------------------------------------------------------------- #


@pytest.mark.smoke
def test_rerank_pairs_are_query_and_chunk_text(fake_st: MagicMock) -> None:
    """The model must receive (query, chunk.text) tuples — not chunk objects."""
    rr = BGERerankerV2()
    rr.rerank("What is X?", _make_chunks(2), top_k=2)

    args, _kwargs = fake_st.predict.call_args
    pairs = args[0]
    assert pairs == [("What is X?", "chunk text 0"), ("What is X?", "chunk text 1")]


@pytest.mark.smoke
def test_rerank_passes_batch_size(fake_st: MagicMock) -> None:
    rr = BGERerankerV2(batch_size=4)
    rr.rerank("q", _make_chunks(3), top_k=3)

    _args, kwargs = fake_st.predict.call_args
    assert kwargs.get("batch_size") == 4


# --------------------------------------------------------------------------- #
# Custom config
# --------------------------------------------------------------------------- #


@pytest.mark.smoke
def test_custom_model_name_passed_to_cross_encoder(monkeypatch: pytest.MonkeyPatch) -> None:
    captured: dict[str, Any] = {}

    def fake_cls(name: str, **kw: Any) -> MagicMock:
        captured["name"] = name
        captured["kw"] = kw
        m = MagicMock()
        m.predict.side_effect = lambda pairs, **_kw: np.zeros(len(pairs))
        return m

    fake_module = MagicMock()
    fake_module.CrossEncoder.side_effect = fake_cls
    monkeypatch.setitem(sys.modules, "sentence_transformers", fake_module)

    rr = BGERerankerV2(model_name="custom/reranker", max_length=256, device="cpu")
    rr.rerank("q", _make_chunks(1), top_k=1)

    assert captured["name"] == "custom/reranker"
    assert captured["kw"]["max_length"] == 256
    assert captured["kw"]["device"] == "cpu"


# --------------------------------------------------------------------------- #
# Slow integration test — real BGE rerank model
# --------------------------------------------------------------------------- #


@pytest.mark.slow
def test_real_bge_reranker_orders_relevant_first() -> None:
    pytest.importorskip("sentence_transformers")
    rr = BGERerankerV2(model_name="BAAI/bge-reranker-v2-m3")

    chunks = [
        RetrievedChunk(
            chunk=Chunk(
                chunk_id="doc::ch0",
                text="The capital of France is Paris.",
                doc_id="doc",
                sentence_ids=("doc::s0",),
                span=Span(doc_id="doc", char_start=0, char_end=30),
                metadata={"section_id": "doc::sec0", "paragraph_id": "doc::p0"},
            ),
            score=0.5,
            retrieval_method="hybrid",
        ),
        RetrievedChunk(
            chunk=Chunk(
                chunk_id="doc::ch1",
                text="Bananas are a type of berry.",
                doc_id="doc",
                sentence_ids=("doc::s1",),
                span=Span(doc_id="doc", char_start=31, char_end=58),
                metadata={"section_id": "doc::sec0", "paragraph_id": "doc::p1"},
            ),
            score=0.4,
            retrieval_method="hybrid",
        ),
    ]
    out = rr.rerank("What is the capital of France?", chunks, top_k=2)
    assert out[0].chunk.chunk_id == "doc::ch0"
