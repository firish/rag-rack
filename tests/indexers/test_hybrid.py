"""HybridIndex + RRF fusion tests.

Uses real LanceDB and bm25s — both are skipped if not installed.  The dense
sub-index gets tiny 4-dim unit vectors; the sparse sub-index uses real text.
"""
from __future__ import annotations

import math
from pathlib import Path

import pytest

from tests.chunkers.conftest import build_document
from verifiable_rag.chunkers import ParentChildChunker
from verifiable_rag.indexers import BM25Index, HybridIndex, LanceDBIndex
from verifiable_rag.indexers.hybrid import _rrf_fuse
from verifiable_rag.models.chunk import Chunk, RetrievedChunk
from verifiable_rag.models.span import Span

lancedb = pytest.importorskip("lancedb", reason="lancedb not installed")
bm25s = pytest.importorskip("bm25s", reason="bm25s not installed")

DIM = 4


def _unit_vec(values: list[float]) -> list[float]:
    mag = math.sqrt(sum(v * v for v in values))
    return [v / mag for v in values]


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


def _make_embeddings(chunks: list[Chunk]) -> list[list[float]]:
    vecs = []
    for i, _ in enumerate(chunks):
        raw = [float(i == j % DIM) + 0.01 for j in range(DIM)]
        vecs.append(_unit_vec(raw))
    return vecs


def _make_hybrid(tmp_path: Path) -> HybridIndex:
    return HybridIndex(
        dense=LanceDBIndex(uri=tmp_path),
        sparse=BM25Index(),
    )


# --------------------------------------------------------------------------- #
# Unit tests for _rrf_fuse
# --------------------------------------------------------------------------- #


@pytest.mark.smoke
def test_rrf_fuse_single_list() -> None:
    """RRF over one list should rank in original order."""
    chunks = _make_chunks(3)
    ranked = [
        RetrievedChunk(chunk=chunks[0], score=0.9, retrieval_method="dense"),
        RetrievedChunk(chunk=chunks[1], score=0.7, retrieval_method="dense"),
        RetrievedChunk(chunk=chunks[2], score=0.5, retrieval_method="dense"),
    ]
    fused = _rrf_fuse([ranked])
    ids = [r.chunk.chunk_id for r in fused]
    assert ids == ["doc::ch0", "doc::ch1", "doc::ch2"]


@pytest.mark.smoke
def test_rrf_fuse_deduplicates_chunks() -> None:
    """A chunk in both lists should appear once in the output."""
    chunks = _make_chunks(2)
    rc0 = RetrievedChunk(chunk=chunks[0], score=0.9, retrieval_method="dense")
    rc1 = RetrievedChunk(chunk=chunks[1], score=0.8, retrieval_method="sparse")
    fused = _rrf_fuse([[rc0, rc1], [rc0, rc1]])
    ids = [r.chunk.chunk_id for r in fused]
    assert len(ids) == len(set(ids))


@pytest.mark.smoke
def test_rrf_fuse_boosts_chunk_in_both_lists() -> None:
    """A chunk ranked well in both lists should outscore one ranked in only one."""
    chunks = _make_chunks(3)
    list_a = [
        RetrievedChunk(chunk=chunks[0], score=0.9, retrieval_method="dense"),
        RetrievedChunk(chunk=chunks[1], score=0.5, retrieval_method="dense"),
    ]
    # chunks[1] is rank-1 in list_b; chunks[2] is rank-2 (only in list_b)
    list_b = [
        RetrievedChunk(chunk=chunks[1], score=0.95, retrieval_method="sparse"),
        RetrievedChunk(chunk=chunks[2], score=0.8, retrieval_method="sparse"),
    ]
    fused = _rrf_fuse([list_a, list_b])
    # chunks[1] appears in both lists (rank 2 + rank 1) → should beat chunks[0] (rank 1 only)
    top_ids = [r.chunk.chunk_id for r in fused[:2]]
    assert "doc::ch1" in top_ids
    assert fused[0].chunk.chunk_id == "doc::ch1"


@pytest.mark.smoke
def test_rrf_fuse_sets_hybrid_retrieval_method() -> None:
    chunks = _make_chunks(2)
    ranked = [RetrievedChunk(chunk=c, score=1.0, retrieval_method="dense") for c in chunks]
    fused = _rrf_fuse([ranked])
    assert all(r.retrieval_method == "hybrid" for r in fused)


@pytest.mark.smoke
def test_rrf_fuse_empty_lists_returns_empty() -> None:
    assert _rrf_fuse([[], []]) == []


# --------------------------------------------------------------------------- #
# HybridIndex construction
# --------------------------------------------------------------------------- #


@pytest.mark.smoke
def test_invalid_rrf_k_raises(tmp_path: Path) -> None:
    with pytest.raises(ValueError, match="rrf_k"):
        HybridIndex(dense=LanceDBIndex(uri=tmp_path), sparse=BM25Index(), rrf_k=0)


@pytest.mark.smoke
def test_invalid_over_fetch_raises(tmp_path: Path) -> None:
    with pytest.raises(ValueError, match="over_fetch"):
        HybridIndex(dense=LanceDBIndex(uri=tmp_path), sparse=BM25Index(), over_fetch=0)


# --------------------------------------------------------------------------- #
# add() and count
# --------------------------------------------------------------------------- #


@pytest.mark.smoke
def test_add_populates_both_indexes(tmp_path: Path) -> None:
    idx = _make_hybrid(tmp_path)
    chunks = _make_chunks(5)
    idx.add(chunks, _make_embeddings(chunks))
    assert idx.count == 5


@pytest.mark.smoke
def test_add_empty_is_noop(tmp_path: Path) -> None:
    idx = _make_hybrid(tmp_path)
    idx.add([], [])
    assert idx.count == 0


# --------------------------------------------------------------------------- #
# search()
# --------------------------------------------------------------------------- #


@pytest.mark.smoke
def test_search_returns_k_results(tmp_path: Path) -> None:
    idx = _make_hybrid(tmp_path)
    chunks = _make_chunks(10)
    idx.add(chunks, _make_embeddings(chunks))
    results = idx.search("content topic", _unit_vec([1.0, 0.0, 0.0, 0.0]), k=3)
    assert len(results) == 3


@pytest.mark.smoke
def test_search_returns_fewer_than_k_when_small(tmp_path: Path) -> None:
    idx = _make_hybrid(tmp_path)
    chunks = _make_chunks(2)
    idx.add(chunks, _make_embeddings(chunks))
    results = idx.search("content topic", _unit_vec([1.0, 0.0, 0.0, 0.0]), k=10)
    assert len(results) == 2


@pytest.mark.smoke
def test_search_empty_index_returns_empty(tmp_path: Path) -> None:
    idx = _make_hybrid(tmp_path)
    results = idx.search("anything", _unit_vec([1.0, 0.0, 0.0, 0.0]), k=5)
    assert results == []


@pytest.mark.smoke
def test_search_scores_are_in_descending_order(tmp_path: Path) -> None:
    idx = _make_hybrid(tmp_path)
    chunks = _make_chunks(6)
    idx.add(chunks, _make_embeddings(chunks))
    results = idx.search("content topic sentence", _unit_vec([1.0, 0.0, 0.0, 0.0]), k=6)
    scores = [r.score for r in results]
    assert scores == sorted(scores, reverse=True)


@pytest.mark.smoke
def test_retrieval_method_is_hybrid(tmp_path: Path) -> None:
    idx = _make_hybrid(tmp_path)
    chunks = _make_chunks(3)
    idx.add(chunks, _make_embeddings(chunks))
    results = idx.search("content", _unit_vec([1.0, 0.0, 0.0, 0.0]), k=3)
    assert all(r.retrieval_method == "hybrid" for r in results)


@pytest.mark.smoke
def test_search_no_duplicates(tmp_path: Path) -> None:
    """Each chunk_id must appear at most once in results."""
    idx = _make_hybrid(tmp_path)
    chunks = _make_chunks(5)
    idx.add(chunks, _make_embeddings(chunks))
    results = idx.search("content topic", _unit_vec([1.0, 0.0, 0.0, 0.0]), k=5)
    ids = [r.chunk.chunk_id for r in results]
    assert len(ids) == len(set(ids))


# --------------------------------------------------------------------------- #
# clear()
# --------------------------------------------------------------------------- #


@pytest.mark.smoke
def test_clear_empties_both_indexes(tmp_path: Path) -> None:
    idx = _make_hybrid(tmp_path)
    chunks = _make_chunks(3)
    idx.add(chunks, _make_embeddings(chunks))
    idx.clear()
    assert idx.count == 0
    assert idx.search("content", _unit_vec([1.0, 0.0, 0.0, 0.0]), k=5) == []


# --------------------------------------------------------------------------- #
# Integration with real chunker output
# --------------------------------------------------------------------------- #


@pytest.mark.smoke
def test_end_to_end_with_chunker_output(tmp_path: Path) -> None:
    import random

    doc = build_document(
        sections_spec=[
            ("Intro", [["Alpha sentence.", "Beta sentence."], ["Gamma sentence."]]),
            ("Methods", [["Delta sentence.", "Epsilon sentence."]]),
        ],
    )
    chunks = ParentChildChunker().chunk(doc)
    random.seed(42)
    embeddings = [_unit_vec([random.random() for _ in range(DIM)]) for _ in chunks]

    idx = _make_hybrid(tmp_path)
    idx.add(chunks, embeddings)
    assert idx.count == len(chunks)

    results = idx.search("Alpha Beta", embeddings[0], k=2)
    assert len(results) >= 1
    assert all(r.retrieval_method == "hybrid" for r in results)
