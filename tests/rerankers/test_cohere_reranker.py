"""CohereReranker tests — fully mocked."""
from __future__ import annotations

import sys
from types import SimpleNamespace
from unittest.mock import MagicMock

import pytest

from verifiable_rag.models.chunk import Chunk, RetrievedChunk
from verifiable_rag.models.span import Span
from verifiable_rag.rerankers import CohereReranker, Reranker


def _chunk(i: int, text: str) -> RetrievedChunk:
    return RetrievedChunk(
        chunk=Chunk(
            chunk_id=f"doc::ch{i}",
            text=text,
            doc_id="doc",
            sentence_ids=(f"doc::s{i}",),
            span=Span(doc_id="doc", char_start=i * 10, char_end=i * 10 + 9),
            metadata={},
        ),
        score=0.5,
        retrieval_method="hybrid",
    )


@pytest.fixture
def fake_cohere(monkeypatch: pytest.MonkeyPatch) -> MagicMock:
    fake_module = MagicMock(name="cohere_module")
    client = MagicMock(name="cohere_client")

    def _rerank(*, model, query, documents, top_n):  # noqa: ANN001
        # Reverse order — chunk N-1 is most relevant, descending.
        n = min(top_n, len(documents))
        results = [
            SimpleNamespace(index=i, relevance_score=1.0 - i / 10.0)
            for i in range(n)
        ]
        return SimpleNamespace(results=results)

    client.rerank.side_effect = _rerank
    fake_module.ClientV2.return_value = client
    monkeypatch.setitem(sys.modules, "cohere", fake_module)
    return client


@pytest.mark.smoke
def test_satisfies_reranker_protocol(fake_cohere: MagicMock) -> None:
    assert isinstance(CohereReranker(api_key="x"), Reranker)


@pytest.mark.smoke
def test_rerank_returns_top_k_in_score_order(fake_cohere: MagicMock) -> None:
    chunks = [_chunk(i, f"chunk {i}") for i in range(10)]
    r = CohereReranker(api_key="x")
    out = r.rerank("query", chunks, top_k=3)
    assert len(out) == 3
    # Scores descending
    assert out[0].score > out[1].score > out[2].score
    # retrieval_method updated
    assert all(rc.retrieval_method == "reranked" for rc in out)


@pytest.mark.smoke
def test_rerank_empty_returns_empty(fake_cohere: MagicMock) -> None:
    r = CohereReranker(api_key="x")
    assert r.rerank("q", [], top_k=5) == []
    fake_cohere.rerank.assert_not_called()


@pytest.mark.smoke
def test_top_k_zero_returns_empty(fake_cohere: MagicMock) -> None:
    chunks = [_chunk(0, "x")]
    r = CohereReranker(api_key="x")
    assert r.rerank("q", chunks, top_k=0) == []


@pytest.mark.smoke
def test_top_k_caps_at_input_size(fake_cohere: MagicMock) -> None:
    chunks = [_chunk(i, f"c{i}") for i in range(3)]
    r = CohereReranker(api_key="x")
    out = r.rerank("q", chunks, top_k=10)
    assert len(out) == 3


@pytest.mark.smoke
def test_over_100_chunks_rejected(fake_cohere: MagicMock) -> None:
    chunks = [_chunk(i, f"c{i}") for i in range(101)]
    r = CohereReranker(api_key="x")
    with pytest.raises(ValueError, match="at most 100"):
        r.rerank("q", chunks, top_k=5)


@pytest.mark.smoke
def test_missing_api_key_raises_at_use(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("COHERE_API_KEY", raising=False)
    r = CohereReranker(api_key=None)
    chunks = [_chunk(0, "x")]
    with pytest.raises(RuntimeError, match="COHERE_API_KEY"):
        r.rerank("q", chunks, top_k=1)
