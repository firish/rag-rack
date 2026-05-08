"""ParentExpander tests.

Coverage focus:
  - section_or_window picks section when it fits, window when it doesn't.
  - Pure section/window strategies bypass the cap check.
  - Window is symmetric, clipped at section edges.
  - Wrong-doc / missing-metadata errors fail loudly (silent miscitation > loud failure).
"""

from __future__ import annotations

import pytest

from tests.chunkers.conftest import build_document
from verifiable_rag.chunkers import ParentChildChunker, ParentExpander

# --------------------------------------------------------------------------- #
# section_or_window: the default strategy
# --------------------------------------------------------------------------- #


@pytest.mark.smoke
def test_returns_full_section_when_under_cap() -> None:
    doc = build_document(
        sections_spec=[("Intro", [["A1.", "A2."], ["B1."]])],
    )
    chunks = ParentChildChunker().chunk(doc)
    expander = ParentExpander(max_parent_tokens=10_000)

    parent = expander.expand(chunks[0], doc)
    # Full section text contains both paragraphs joined by "\n\n"
    assert "A1. A2." in parent
    assert "B1." in parent


@pytest.mark.smoke
def test_falls_back_to_window_when_section_too_big() -> None:
    """Section exceeds max_parent_tokens → return symmetric window."""
    big_section_paras = [[f"Para{i} sentence."] for i in range(20)]
    doc = build_document(sections_spec=[("Huge", big_section_paras)])
    chunks = ParentChildChunker().chunk(doc)

    # Pick the chunk for paragraph 10 (middle of section)
    target = chunks[10]
    expander = ParentExpander(
        max_parent_tokens=10,  # forces window fallback
        window_paragraphs=2,
    )
    parent = expander.expand(target, doc)

    # Window of 2 each side → 5 paragraphs (8, 9, 10, 11, 12)
    assert "Para8 sentence." in parent
    assert "Para12 sentence." in parent
    assert "Para7 sentence." not in parent
    assert "Para13 sentence." not in parent


# --------------------------------------------------------------------------- #
# Strategy: "section" — never windowed
# --------------------------------------------------------------------------- #


@pytest.mark.smoke
def test_section_strategy_ignores_cap() -> None:
    """Even with a tiny cap, 'section' strategy returns the whole section."""
    paras = [[f"Para{i}."] for i in range(10)]
    doc = build_document(sections_spec=[("All", paras)])
    chunks = ParentChildChunker().chunk(doc)

    expander = ParentExpander(strategy="section", max_parent_tokens=1)
    parent = expander.expand(chunks[5], doc)
    for i in range(10):
        assert f"Para{i}." in parent


# --------------------------------------------------------------------------- #
# Strategy: "window" — predictable size
# --------------------------------------------------------------------------- #


@pytest.mark.smoke
def test_window_strategy_returns_symmetric_neighbors() -> None:
    paras = [[f"P{i}."] for i in range(10)]
    doc = build_document(sections_spec=[("S", paras)])
    chunks = ParentChildChunker().chunk(doc)

    expander = ParentExpander(strategy="window", window_paragraphs=2)
    parent = expander.expand(chunks[5], doc)
    # Should contain P3, P4, P5, P6, P7
    for i in (3, 4, 5, 6, 7):
        assert f"P{i}." in parent
    for i in (2, 8):
        assert f"P{i}." not in parent


@pytest.mark.smoke
def test_window_clips_at_section_start() -> None:
    paras = [[f"P{i}."] for i in range(10)]
    doc = build_document(sections_spec=[("S", paras)])
    chunks = ParentChildChunker().chunk(doc)

    # Chunk for paragraph 0 — window should be [0, 1, 2] only
    expander = ParentExpander(strategy="window", window_paragraphs=2)
    parent = expander.expand(chunks[0], doc)
    for i in (0, 1, 2):
        assert f"P{i}." in parent
    assert "P3." not in parent


@pytest.mark.smoke
def test_window_clips_at_section_end() -> None:
    paras = [[f"P{i}."] for i in range(5)]
    doc = build_document(sections_spec=[("S", paras)])
    chunks = ParentChildChunker().chunk(doc)

    # Chunk for paragraph 4 (last) — window should be [2, 3, 4]
    expander = ParentExpander(strategy="window", window_paragraphs=2)
    parent = expander.expand(chunks[4], doc)
    for i in (2, 3, 4):
        assert f"P{i}." in parent


@pytest.mark.smoke
def test_window_zero_returns_only_self_paragraph() -> None:
    paras = [[f"P{i}."] for i in range(5)]
    doc = build_document(sections_spec=[("S", paras)])
    chunks = ParentChildChunker().chunk(doc)

    expander = ParentExpander(strategy="window", window_paragraphs=0)
    parent = expander.expand(chunks[2], doc)
    assert parent == "P2."


# --------------------------------------------------------------------------- #
# Multi-section docs: parent expansion stays within the chunk's section
# --------------------------------------------------------------------------- #


@pytest.mark.smoke
def test_window_stays_within_section_boundary() -> None:
    """A chunk's window never bleeds into adjacent sections."""
    doc = build_document(
        sections_spec=[
            ("Sec1", [["A1."], ["A2."], ["A3."]]),
            ("Sec2", [["B1."], ["B2."]]),
        ],
    )
    chunks = ParentChildChunker().chunk(doc)
    # Chunk for last paragraph of Sec1 (index 2 globally)
    expander = ParentExpander(strategy="window", window_paragraphs=3)
    parent = expander.expand(chunks[2], doc)
    # Sec2 content must NOT appear
    assert "B1." not in parent
    assert "B2." not in parent
    # All Sec1 paragraphs should
    for i in (1, 2, 3):
        assert f"A{i}." in parent


# --------------------------------------------------------------------------- #
# Validation
# --------------------------------------------------------------------------- #


@pytest.mark.smoke
def test_doc_id_mismatch_raises() -> None:
    doc1 = build_document(sections_spec=[(None, [["x."]])], doc_id="d1")
    doc2 = build_document(sections_spec=[(None, [["y."]])], doc_id="d2")
    chunk = ParentChildChunker().chunk(doc1)[0]

    with pytest.raises(ValueError, match="doc_id"):
        ParentExpander().expand(chunk, doc2)


@pytest.mark.smoke
def test_missing_section_id_metadata_raises() -> None:
    """A chunk produced by a different chunker (no section_id) fails loudly."""
    from verifiable_rag.models.chunk import Chunk
    from verifiable_rag.models.span import Span

    doc = build_document(sections_spec=[(None, [["only."]])])
    bad_chunk = Chunk(
        chunk_id="bad::ch0",
        text="only.",
        doc_id=doc.doc_id,
        sentence_ids=("doctest::s0",),
        span=Span(doc_id=doc.doc_id, char_start=0, char_end=5),
        metadata={},  # no section_id, no paragraph_id
    )
    with pytest.raises(ValueError, match="section_id"):
        ParentExpander().expand(bad_chunk, doc)


@pytest.mark.smoke
def test_unknown_section_id_raises() -> None:
    from verifiable_rag.models.chunk import Chunk
    from verifiable_rag.models.span import Span

    doc = build_document(sections_spec=[(None, [["only."]])])
    bad_chunk = Chunk(
        chunk_id="bad::ch0",
        text="only.",
        doc_id=doc.doc_id,
        sentence_ids=("doctest::s0",),
        span=Span(doc_id=doc.doc_id, char_start=0, char_end=5),
        metadata={"section_id": "doctest::sec999", "paragraph_id": "x"},
    )
    with pytest.raises(KeyError, match="sec999"):
        ParentExpander().expand(bad_chunk, doc)


@pytest.mark.smoke
def test_invalid_constructor_args_raise() -> None:
    with pytest.raises(ValueError, match="max_parent_tokens"):
        ParentExpander(max_parent_tokens=0)
    with pytest.raises(ValueError, match="window_paragraphs"):
        ParentExpander(window_paragraphs=-1)
