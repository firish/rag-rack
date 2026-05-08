"""BM25Index tests.

All tests use real bm25s (no mocking) — the library is pure Python and fast
enough for CI.  Tests are gated by pytest.importorskip so they are skipped
cleanly if bm25s is not installed.
"""
from __future__ import annotations

import pytest

from tests.chunkers.conftest import build_document
from verifiable_rag.chunkers import ParentChildChunker
from verifiable_rag.indexers import SparseIndex
from verifiable_rag.indexers.sparse.bm25 import BM25Index
from verifiable_rag.models.chunk import Chunk
from verifiable_rag.models.span import Span

bm25s = pytest.importorskip("bm25s", reason="bm25s not installed")


# --------------------------------------------------------------------------- #
# Helpers
# --------------------------------------------------------------------------- #


def _make_chunks(n: int, doc_id: str = "doc") -> list[Chunk]:
    return [
        Chunk(
            chunk_id=f"{doc_id}::ch{i}",
            text=f"Sentence {i} content about topic {i}.",
            doc_id=doc_id,
            sentence_ids=(f"{doc_id}::s{i}",),
            span=Span(doc_id=doc_id, char_start=i * 20, char_end=i * 20 + 19),
            metadata={"section_id": f"{doc_id}::sec0", "paragraph_id": f"{doc_id}::para{i}"},
        )
        for i in range(n)
    ]


# --------------------------------------------------------------------------- #
# Protocol conformance
# --------------------------------------------------------------------------- #


@pytest.mark.smoke
def test_satisfies_sparse_index_protocol() -> None:
    idx = BM25Index()
    assert isinstance(idx, SparseIndex)


# --------------------------------------------------------------------------- #
# add() and count
# --------------------------------------------------------------------------- #


@pytest.mark.smoke
def test_add_populates_index() -> None:
    idx = BM25Index()
    idx.add(_make_chunks(5))
    assert idx.count == 5


@pytest.mark.smoke
def test_add_empty_is_noop() -> None:
    idx = BM25Index()
    idx.add([])
    assert idx.count == 0


@pytest.mark.smoke
def test_add_appends_on_second_call() -> None:
    idx = BM25Index()
    idx.add(_make_chunks(3))
    idx.add(_make_chunks(2, doc_id="doc2"))
    assert idx.count == 5


# --------------------------------------------------------------------------- #
# search()
# --------------------------------------------------------------------------- #


@pytest.mark.smoke
def test_search_returns_k_results() -> None:
    idx = BM25Index()
    idx.add(_make_chunks(10))
    results = idx.search("content topic", k=3)
    assert len(results) == 3


@pytest.mark.smoke
def test_search_returns_fewer_than_k_when_small() -> None:
    idx = BM25Index()
    idx.add(_make_chunks(2))
    results = idx.search("content topic", k=10)
    assert len(results) == 2


@pytest.mark.smoke
def test_search_empty_index_returns_empty() -> None:
    idx = BM25Index()
    results = idx.search("anything", k=5)
    assert results == []


@pytest.mark.smoke
def test_search_top_result_is_most_relevant() -> None:
    """Chunk with exact keyword match should rank first."""
    idx = BM25Index()
    chunks = [
        Chunk(
            chunk_id="doc::ch0",
            text="The mitochondria is the powerhouse of the cell.",
            doc_id="doc",
            sentence_ids=("doc::s0",),
            span=Span(doc_id="doc", char_start=0, char_end=45),
            metadata={"section_id": "doc::sec0", "paragraph_id": "doc::para0"},
        ),
        Chunk(
            chunk_id="doc::ch1",
            text="Neural networks learn hierarchical representations.",
            doc_id="doc",
            sentence_ids=("doc::s1",),
            span=Span(doc_id="doc", char_start=46, char_end=95),
            metadata={"section_id": "doc::sec0", "paragraph_id": "doc::para1"},
        ),
        Chunk(
            chunk_id="doc::ch2",
            text="Photosynthesis converts sunlight into glucose.",
            doc_id="doc",
            sentence_ids=("doc::s2",),
            span=Span(doc_id="doc", char_start=96, char_end=141),
            metadata={"section_id": "doc::sec0", "paragraph_id": "doc::para2"},
        ),
    ]
    idx.add(chunks)
    results = idx.search("mitochondria cell powerhouse", k=3)
    assert results[0].chunk.chunk_id == "doc::ch0"


@pytest.mark.smoke
def test_search_scores_are_non_negative() -> None:
    idx = BM25Index()
    idx.add(_make_chunks(5))
    results = idx.search("content topic sentence", k=5)
    assert all(r.score >= 0.0 for r in results)


@pytest.mark.smoke
def test_search_scores_are_in_descending_order() -> None:
    idx = BM25Index()
    idx.add(_make_chunks(5))
    results = idx.search("content topic sentence", k=5)
    scores = [r.score for r in results]
    assert scores == sorted(scores, reverse=True)


@pytest.mark.smoke
def test_retrieval_method_is_sparse() -> None:
    idx = BM25Index()
    idx.add(_make_chunks(3))
    results = idx.search("content", k=3)
    assert all(r.retrieval_method == "sparse" for r in results)


# --------------------------------------------------------------------------- #
# Chunk round-trip
# --------------------------------------------------------------------------- #


@pytest.mark.smoke
def test_chunk_roundtrip_preserves_all_fields() -> None:
    from verifiable_rag.models.span import BBox, PageBBox

    bb = PageBBox(page=1, bbox=BBox(x0=5.0, y0=10.0, x1=100.0, y1=20.0))
    original = Chunk(
        chunk_id="test::ch0",
        text="Some specific text for BM25 roundtrip.",
        doc_id="test",
        sentence_ids=("test::s0", "test::s1"),
        span=Span(doc_id="test", char_start=0, char_end=37, bboxes=(bb,)),
        metadata={"section_id": "test::sec0", "paragraph_id": "test::para0", "page_first": 1},
    )
    idx = BM25Index()
    idx.add([original])
    results = idx.search("specific text BM25 roundtrip", k=1)
    assert len(results) == 1
    got = results[0].chunk

    assert got.chunk_id == original.chunk_id
    assert got.text == original.text
    assert got.doc_id == original.doc_id
    assert got.sentence_ids == original.sentence_ids
    assert got.span.char_start == original.span.char_start
    assert got.span.char_end == original.span.char_end
    assert len(got.span.bboxes) == 1
    assert got.span.bboxes[0].page == 1
    assert got.span.bboxes[0].bbox.x0 == pytest.approx(5.0)
    assert got.metadata == original.metadata


# --------------------------------------------------------------------------- #
# clear()
# --------------------------------------------------------------------------- #


@pytest.mark.smoke
def test_clear_removes_all_data() -> None:
    idx = BM25Index()
    idx.add(_make_chunks(3))
    idx.clear()
    assert idx.count == 0
    assert idx.search("content", k=5) == []


# --------------------------------------------------------------------------- #
# save() / load()
# --------------------------------------------------------------------------- #


@pytest.mark.smoke
def test_save_and_load_round_trip(tmp_path: "Path") -> None:  # noqa: F821
    from pathlib import Path

    idx = BM25Index()
    chunks = _make_chunks(4)
    idx.add(chunks)
    idx.save(tmp_path / "bm25_test")

    loaded = BM25Index.load(tmp_path / "bm25_test")
    assert loaded.count == 4
    results = loaded.search("content topic", k=2)
    assert len(results) == 2


# --------------------------------------------------------------------------- #
# Integration with real chunker output
# --------------------------------------------------------------------------- #


@pytest.mark.smoke
def test_end_to_end_with_chunker_output() -> None:
    doc = build_document(
        sections_spec=[
            ("Intro", [["Alpha sentence.", "Beta sentence."], ["Gamma sentence."]]),
            ("Methods", [["Delta sentence.", "Epsilon sentence."]]),
        ],
    )
    chunks = ParentChildChunker().chunk(doc)
    idx = BM25Index()
    idx.add(chunks)
    assert idx.count == len(chunks)

    results = idx.search("Alpha Beta", k=2)
    assert len(results) >= 1
    # The chunk containing "Alpha sentence. Beta sentence." should be top result
    assert "Alpha" in results[0].chunk.text or "Beta" in results[0].chunk.text
