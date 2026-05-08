"""ParentChildChunker tests.

Coverage focus:
  - One-paragraph-one-chunk for the common (small) case.
  - Sentence-aligned splitting when paragraphs exceed the cap.
  - Single oversized sentences emitted as their own chunk (atomicity).
  - Sentence-id coverage and ordering preserved exactly across all chunks.
  - Required parent-pointer metadata is populated on every chunk.
"""

from __future__ import annotations

import pytest

from tests.chunkers.conftest import assert_chunk_invariants, build_document
from verifiable_rag.chunkers import Chunker, ParentChildChunker

# --------------------------------------------------------------------------- #
# Constructor validation
# --------------------------------------------------------------------------- #


@pytest.mark.smoke
def test_chunker_satisfies_protocol() -> None:
    """ParentChildChunker is structurally a Chunker — important for swap-in."""
    assert isinstance(ParentChildChunker(), Chunker)


@pytest.mark.smoke
def test_invalid_max_child_tokens_raises() -> None:
    with pytest.raises(ValueError, match="max_child_tokens"):
        ParentChildChunker(max_child_tokens=0)


# --------------------------------------------------------------------------- #
# Common case: one paragraph → one chunk
# --------------------------------------------------------------------------- #


@pytest.mark.smoke
def test_small_paragraph_becomes_single_chunk() -> None:
    doc = build_document(
        sections_spec=[
            ("Intro", [["Alpha.", "Beta.", "Gamma."]]),
        ],
    )
    chunks = ParentChildChunker(max_child_tokens=400).chunk(doc)

    assert len(chunks) == 1
    assert chunks[0].text == "Alpha. Beta. Gamma."
    assert chunks[0].sentence_ids == ("doctest::s0", "doctest::s1", "doctest::s2")
    assert_chunk_invariants(doc, chunks)


@pytest.mark.smoke
def test_one_chunk_per_paragraph_when_all_small() -> None:
    doc = build_document(
        sections_spec=[
            ("Intro", [["A1.", "A2."], ["B1."]]),
            ("Methods", [["C1.", "C2.", "C3."]]),
        ],
    )
    chunks = ParentChildChunker(max_child_tokens=400).chunk(doc)

    assert len(chunks) == 3
    # paragraph_part = 0, paragraph_part_count = 1 when not split
    for ch in chunks:
        assert ch.metadata["paragraph_part"] == 0
        assert ch.metadata["paragraph_part_count"] == 1
    assert_chunk_invariants(doc, chunks)


# --------------------------------------------------------------------------- #
# Splitting: paragraph too large → multiple sentence-aligned chunks
# --------------------------------------------------------------------------- #


@pytest.mark.smoke
def test_oversize_paragraph_splits_at_sentence_boundary() -> None:
    """Cap so small that each sentence becomes its own chunk."""
    sentences = ["Sentence one.", "Sentence two.", "Sentence three.", "Sentence four."]
    doc = build_document(sections_spec=[(None, [sentences])])

    # Each sentence ~13 chars → ~3 tokens with /4 estimator. Cap at 4 tokens
    # forces one sentence per chunk.
    chunks = ParentChildChunker(max_child_tokens=4).chunk(doc)
    assert len(chunks) == 4
    for i, ch in enumerate(chunks):
        assert ch.metadata["paragraph_part"] == i
        assert ch.metadata["paragraph_part_count"] == 4
        assert len(ch.sentence_ids) == 1
    assert_chunk_invariants(doc, chunks)


@pytest.mark.smoke
def test_split_packs_sentences_greedily() -> None:
    """Multiple sentences fit in one chunk before flushing."""
    # 5 short sentences; cap allows ~2 per chunk.
    sentences = ["Aa bb.", "Cc dd.", "Ee ff.", "Gg hh.", "Ii jj."]
    doc = build_document(sections_spec=[(None, [sentences])])

    # Each ~6 chars → ~1 token. Cap of 3 tokens → ~3 sentences per group.
    chunks = ParentChildChunker(max_child_tokens=3).chunk(doc)
    assert len(chunks) >= 2
    # Concatenating chunk sentence_ids in order recovers the document
    flat = [sid for ch in chunks for sid in ch.sentence_ids]
    assert flat == [s.id for s in doc.sentences]
    # paragraph_part_count is consistent across all chunks of this paragraph
    counts = {ch.metadata["paragraph_part_count"] for ch in chunks}
    assert counts == {len(chunks)}
    assert_chunk_invariants(doc, chunks)


@pytest.mark.smoke
def test_oversized_single_sentence_is_emitted_alone() -> None:
    """A sentence above the cap is never split — it gets its own chunk."""
    huge = "Word " * 100  # ~500 chars → ~125 tokens
    doc = build_document(
        sections_spec=[
            (None, [["Tiny.", huge.strip(), "Also tiny."]]),
        ],
    )
    chunks = ParentChildChunker(max_child_tokens=10).chunk(doc)

    # Find the chunk holding the huge sentence
    huge_chunks = [c for c in chunks if any("s1" in sid for sid in c.sentence_ids)]
    assert len(huge_chunks) == 1
    assert huge_chunks[0].sentence_ids == ("doctest::s1",)
    assert_chunk_invariants(doc, chunks)


# --------------------------------------------------------------------------- #
# Metadata pointers — required for ParentExpander to do its job
# --------------------------------------------------------------------------- #


@pytest.mark.smoke
def test_metadata_includes_section_and_paragraph_pointers() -> None:
    doc = build_document(
        sections_spec=[
            ("Intro", [["A1."], ["A2."]]),
            ("Methods", [["B1."]]),
        ],
    )
    chunks = ParentChildChunker().chunk(doc)
    assert len(chunks) == 3
    # First two chunks belong to section 0, third to section 1
    assert chunks[0].metadata["section_id"] == "doctest::sec0"
    assert chunks[1].metadata["section_id"] == "doctest::sec0"
    assert chunks[2].metadata["section_id"] == "doctest::sec1"
    # And to distinct paragraphs
    para_ids = {c.metadata["paragraph_id"] for c in chunks}
    assert len(para_ids) == 3
    # Section title surfaced
    assert chunks[0].metadata["section_title"] == "Intro"
    assert chunks[2].metadata["section_title"] == "Methods"


@pytest.mark.smoke
def test_metadata_pages_match_span() -> None:
    doc = build_document(sections_spec=[(None, [["Hello.", "World."]])])
    chunks = ParentChildChunker().chunk(doc)
    for ch in chunks:
        first, last = doc.pages_for_span(ch.span)
        assert ch.metadata["page_first"] == first
        assert ch.metadata["page_last"] == last


# --------------------------------------------------------------------------- #
# Edge cases
# --------------------------------------------------------------------------- #


@pytest.mark.smoke
def test_empty_document_returns_empty_list() -> None:
    """No sections → no chunks; the chunker doesn't enforce non-empty docs."""
    doc = build_document(sections_spec=[])
    assert ParentChildChunker().chunk(doc) == []


@pytest.mark.smoke
def test_chunk_ids_are_unique_and_ordered() -> None:
    doc = build_document(
        sections_spec=[
            ("S1", [["a."], ["b."]]),
            ("S2", [["c."]]),
        ],
    )
    chunks = ParentChildChunker().chunk(doc)
    ids = [c.chunk_id for c in chunks]
    assert ids == ["doctest::ch0", "doctest::ch1", "doctest::ch2"]
    assert len(set(ids)) == len(ids)


@pytest.mark.smoke
def test_custom_token_counter_is_respected() -> None:
    """A token counter that overestimates forces aggressive splitting."""
    doc = build_document(sections_spec=[(None, [["A.", "B.", "C.", "D."]])])
    # Always reports 100 tokens regardless of input — every sentence triggers a flush
    chunks = ParentChildChunker(max_child_tokens=50, token_count=lambda _t: 100).chunk(doc)
    # First branch (paragraph.text > cap) triggers split path; each sentence
    # also exceeds, so each lands alone.
    assert len(chunks) == 4
    assert_chunk_invariants(doc, chunks)
