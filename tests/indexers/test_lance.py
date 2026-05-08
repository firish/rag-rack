"""LanceDBIndex tests.

Uses real LanceDB with tmp_path for isolation — no mocking needed since the
library is file-backed.  All tests are @pytest.mark.smoke because they run
in <1s each (flat scan, tiny data).
"""
from __future__ import annotations

import math
from pathlib import Path

import pytest

from tests.chunkers.conftest import build_document
from verifiable_rag.chunkers import ParentChildChunker
from verifiable_rag.indexers import DenseIndex, LanceDBIndex
from verifiable_rag.models.chunk import Chunk
from verifiable_rag.models.span import BBox, PageBBox, Span

lancedb = pytest.importorskip("lancedb", reason="lancedb not installed")


# --------------------------------------------------------------------------- #
# Helpers
# --------------------------------------------------------------------------- #

DIM = 4  # tiny dimension for fast tests


def _unit_vec(values: list[float]) -> list[float]:
    mag = math.sqrt(sum(v * v for v in values))
    return [v / mag for v in values]


def _make_chunks(n: int, doc_id: str = "doc") -> list[Chunk]:
    """Produce n minimal Chunks — spans don't need to be real for index tests."""
    return [
        Chunk(
            chunk_id=f"{doc_id}::ch{i}",
            text=f"Sentence {i} content.",
            doc_id=doc_id,
            sentence_ids=(f"{doc_id}::s{i}",),
            span=Span(doc_id=doc_id, char_start=i * 10, char_end=i * 10 + 9),
            metadata={"section_id": f"{doc_id}::sec0", "paragraph_id": f"{doc_id}::para{i}"},
        )
        for i in range(n)
    ]


def _make_embeddings(chunks: list[Chunk]) -> list[list[float]]:
    """One-hot-ish unit vectors — each chunk is clearly distinct."""
    vecs = []
    for i, _ in enumerate(chunks):
        raw = [float(i == j % DIM) + 0.01 for j in range(DIM)]
        vecs.append(_unit_vec(raw))
    return vecs


# --------------------------------------------------------------------------- #
# Protocol conformance
# --------------------------------------------------------------------------- #

@pytest.mark.smoke
def test_satisfies_dense_index_protocol(tmp_path: Path) -> None:
    idx = LanceDBIndex(uri=tmp_path)
    assert isinstance(idx, DenseIndex)


# --------------------------------------------------------------------------- #
# add() and count
# --------------------------------------------------------------------------- #

@pytest.mark.smoke
def test_add_populates_table(tmp_path: Path) -> None:
    idx = LanceDBIndex(uri=tmp_path)
    chunks = _make_chunks(5)
    idx.add(chunks, _make_embeddings(chunks))
    assert idx.count == 5


@pytest.mark.smoke
def test_add_empty_is_noop(tmp_path: Path) -> None:
    idx = LanceDBIndex(uri=tmp_path)
    idx.add([], [])
    assert idx.count == 0


@pytest.mark.smoke
def test_add_length_mismatch_raises(tmp_path: Path) -> None:
    idx = LanceDBIndex(uri=tmp_path)
    chunks = _make_chunks(3)
    with pytest.raises(ValueError, match="mismatch"):
        idx.add(chunks, _make_embeddings(chunks)[:2])


@pytest.mark.smoke
def test_add_appends_to_existing_table(tmp_path: Path) -> None:
    idx = LanceDBIndex(uri=tmp_path)
    batch1 = _make_chunks(3)
    batch2 = _make_chunks(2, doc_id="doc2")
    idx.add(batch1, _make_embeddings(batch1))
    idx.add(batch2, _make_embeddings(batch2))
    assert idx.count == 5


# --------------------------------------------------------------------------- #
# search() — retrieval and ranking
# --------------------------------------------------------------------------- #

@pytest.mark.smoke
def test_search_returns_k_results(tmp_path: Path) -> None:
    idx = LanceDBIndex(uri=tmp_path)
    chunks = _make_chunks(10)
    idx.add(chunks, _make_embeddings(chunks))

    results = idx.search(_unit_vec([1.0, 0.0, 0.0, 0.0]), k=3)
    assert len(results) == 3


@pytest.mark.smoke
def test_search_returns_fewer_than_k_when_table_small(tmp_path: Path) -> None:
    idx = LanceDBIndex(uri=tmp_path)
    chunks = _make_chunks(2)
    idx.add(chunks, _make_embeddings(chunks))

    results = idx.search(_unit_vec([1.0, 0.0, 0.0, 0.0]), k=10)
    assert len(results) == 2


@pytest.mark.smoke
def test_search_empty_index_returns_empty(tmp_path: Path) -> None:
    idx = LanceDBIndex(uri=tmp_path)
    results = idx.search(_unit_vec([1.0, 0.0, 0.0, 0.0]), k=5)
    assert results == []


@pytest.mark.smoke
def test_search_top_result_is_most_similar(tmp_path: Path) -> None:
    """The nearest vector must come back first."""
    idx = LanceDBIndex(uri=tmp_path)
    chunks = _make_chunks(4)
    # chunk 0 → [1, 0, 0, 0], chunk 1 → [0, 1, 0, 0], etc.
    embeddings = [
        _unit_vec([1.0, 0.01, 0.01, 0.01]),
        _unit_vec([0.01, 1.0, 0.01, 0.01]),
        _unit_vec([0.01, 0.01, 1.0, 0.01]),
        _unit_vec([0.01, 0.01, 0.01, 1.0]),
    ]
    idx.add(chunks, embeddings)

    # Query close to chunk 2's direction
    query = _unit_vec([0.01, 0.01, 1.0, 0.01])
    results = idx.search(query, k=4)
    assert results[0].chunk.chunk_id == "doc::ch2"


@pytest.mark.smoke
def test_search_scores_are_in_descending_order(tmp_path: Path) -> None:
    idx = LanceDBIndex(uri=tmp_path)
    chunks = _make_chunks(5)
    idx.add(chunks, _make_embeddings(chunks))

    results = idx.search(_unit_vec([1.0, 0.0, 0.0, 0.0]), k=5)
    scores = [r.score for r in results]
    assert scores == sorted(scores, reverse=True)


@pytest.mark.smoke
def test_search_score_is_bounded(tmp_path: Path) -> None:
    """Cosine score = 1 - distance/2 = cosine_similarity ∈ [-1, 1]."""
    idx = LanceDBIndex(uri=tmp_path)
    chunks = _make_chunks(4)
    idx.add(chunks, _make_embeddings(chunks))

    results = idx.search(_unit_vec([1.0, 0.0, 0.0, 0.0]), k=4)
    for r in results:
        assert -1.01 <= r.score <= 1.01, f"score {r.score} out of expected range"


@pytest.mark.smoke
def test_retrieval_method_is_dense(tmp_path: Path) -> None:
    idx = LanceDBIndex(uri=tmp_path)
    chunks = _make_chunks(2)
    idx.add(chunks, _make_embeddings(chunks))
    results = idx.search(_unit_vec([1.0, 0.0, 0.0, 0.0]), k=2)
    assert all(r.retrieval_method == "dense" for r in results)


# --------------------------------------------------------------------------- #
# Chunk round-trip — what goes in must come out intact
# --------------------------------------------------------------------------- #

@pytest.mark.smoke
def test_chunk_roundtrip_preserves_all_fields(tmp_path: Path) -> None:
    """Every field on the original Chunk must survive the DB round-trip."""
    bb = PageBBox(page=2, bbox=BBox(x0=10.0, y0=20.0, x1=200.0, y1=40.0))
    original = Chunk(
        chunk_id="test::ch0",
        text="Some meaningful text.",
        doc_id="test",
        sentence_ids=("test::s0", "test::s1"),
        span=Span(doc_id="test", char_start=5, char_end=26, bboxes=(bb,)),
        metadata={"section_id": "test::sec0", "paragraph_id": "test::para0", "page_first": 2},
    )
    idx = LanceDBIndex(uri=tmp_path)
    idx.add([original], [_unit_vec([1.0, 0.0, 0.0, 0.0])])

    results = idx.search(_unit_vec([1.0, 0.0, 0.0, 0.0]), k=1)
    assert len(results) == 1
    got = results[0].chunk

    assert got.chunk_id == original.chunk_id
    assert got.text == original.text
    assert got.doc_id == original.doc_id
    assert got.sentence_ids == original.sentence_ids
    assert got.span.char_start == original.span.char_start
    assert got.span.char_end == original.span.char_end
    assert len(got.span.bboxes) == 1
    assert got.span.bboxes[0].page == 2
    assert got.span.bboxes[0].bbox.x0 == pytest.approx(10.0)
    assert got.metadata == original.metadata


# --------------------------------------------------------------------------- #
# Persistence — new instance, same URI, data still there
# --------------------------------------------------------------------------- #

@pytest.mark.smoke
def test_index_persists_across_instances(tmp_path: Path) -> None:
    """Closing and reopening the index must recover all data."""
    chunks = _make_chunks(4)
    embeddings = _make_embeddings(chunks)

    idx1 = LanceDBIndex(uri=tmp_path)
    idx1.add(chunks, embeddings)
    assert idx1.count == 4

    # New instance, same path — should see all 4 rows
    idx2 = LanceDBIndex(uri=tmp_path)
    assert idx2.count == 4
    results = idx2.search(_unit_vec([1.0, 0.0, 0.0, 0.0]), k=2)
    assert len(results) == 2


# --------------------------------------------------------------------------- #
# clear()
# --------------------------------------------------------------------------- #

@pytest.mark.smoke
def test_clear_removes_all_data(tmp_path: Path) -> None:
    idx = LanceDBIndex(uri=tmp_path)
    chunks = _make_chunks(3)
    idx.add(chunks, _make_embeddings(chunks))
    assert idx.count == 3

    idx.clear()
    assert idx.count == 0
    assert idx.search(_unit_vec([1.0, 0.0, 0.0, 0.0]), k=5) == []


# --------------------------------------------------------------------------- #
# Integration with real chunker output
# --------------------------------------------------------------------------- #

@pytest.mark.smoke
def test_end_to_end_with_chunker_output(tmp_path: Path) -> None:
    """Chunks from ParentChildChunker must index and retrieve without errors."""
    doc = build_document(
        sections_spec=[
            ("Intro", [["Alpha sentence.", "Beta sentence."], ["Gamma sentence."]]),
            ("Methods", [["Delta sentence.", "Epsilon sentence."]]),
        ],
    )
    chunks = ParentChildChunker().chunk(doc)
    # Fabricate random unit embeddings (DIM=4 is not real BGE, just a test stand-in)
    import random
    random.seed(42)
    embeddings = [
        _unit_vec([random.random() for _ in range(DIM)]) for _ in chunks
    ]

    idx = LanceDBIndex(uri=tmp_path)
    idx.add(chunks, embeddings)
    assert idx.count == len(chunks)

    results = idx.search(embeddings[0], k=2)
    assert len(results) == 2
    # The top hit should be the first chunk (exact vector match)
    assert results[0].chunk.chunk_id == chunks[0].chunk_id
    assert results[0].score == pytest.approx(1.0, abs=1e-3)
