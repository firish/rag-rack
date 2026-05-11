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


@pytest.mark.smoke
def test_invalid_min_child_tokens_raises() -> None:
    with pytest.raises(ValueError, match="min_child_tokens"):
        ParentChildChunker(min_child_tokens=-1)


@pytest.mark.smoke
def test_min_above_max_raises() -> None:
    with pytest.raises(ValueError, match="cannot exceed"):
        ParentChildChunker(max_child_tokens=100, min_child_tokens=200)


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


# --------------------------------------------------------------------------- #
# min_child_tokens — cross-paragraph merging
# --------------------------------------------------------------------------- #


@pytest.mark.smoke
def test_min_zero_preserves_legacy_behavior() -> None:
    """min=0 (default) must produce identical output to the original chunker."""
    doc = build_document(
        sections_spec=[
            ("S1", [["A."], ["B."], ["C."]]),  # three single-sentence paras
        ],
    )
    legacy = ParentChildChunker().chunk(doc)
    explicit_zero = ParentChildChunker(min_child_tokens=0).chunk(doc)

    assert len(legacy) == 3
    assert len(explicit_zero) == 3
    assert [c.sentence_ids for c in legacy] == [c.sentence_ids for c in explicit_zero]


@pytest.mark.smoke
def test_min_merges_consecutive_small_paragraphs() -> None:
    """Single-sentence paragraphs below the floor get merged into one chunk."""
    # Each "X." sentence is ~3 chars / 4 ≈ 1 token. Floor of 5 forces merging.
    doc = build_document(
        sections_spec=[
            ("S1", [["A."], ["B."], ["C."], ["D."], ["E."], ["F."]]),
        ],
    )
    chunks = ParentChildChunker(
        max_child_tokens=400,
        min_child_tokens=5,
        token_count=lambda t: max(1, len(t) // 4),
    ).chunk(doc)

    # All 6 single-sentence paragraphs should fold into one chunk
    assert len(chunks) == 1
    assert chunks[0].sentence_ids == tuple(f"doctest::s{i}" for i in range(6))
    assert_chunk_invariants(doc, chunks)


@pytest.mark.smoke
def test_min_does_not_force_merging_when_each_paragraph_already_fills_max() -> None:
    """When each paragraph already saturates max, no cross-paragraph merging."""
    # Each sentence is forced to ~50 tokens; max=50, floor=20.
    # Adding a second paragraph would overflow max → flush each alone.
    doc = build_document(
        sections_spec=[
            ("S1", [["Para A sentence."], ["Para B sentence."], ["Para C sentence."]]),
        ],
    )
    chunks = ParentChildChunker(
        max_child_tokens=50,
        min_child_tokens=20,
        token_count=lambda _t: 50,
    ).chunk(doc)

    assert len(chunks) == 3


@pytest.mark.smoke
def test_min_does_not_merge_across_sections() -> None:
    """Section boundaries are hard — even when both sections are tiny."""
    doc = build_document(
        sections_spec=[
            ("S1", [["A."]]),  # 1 sentence in section 1
            ("S2", [["B."]]),  # 1 sentence in section 2
        ],
    )
    chunks = ParentChildChunker(
        max_child_tokens=400,
        min_child_tokens=100,  # neither section meets the floor
        token_count=lambda t: max(1, len(t) // 4),
    ).chunk(doc)

    # Two chunks (one per section), each under-floor — better than dropping.
    assert len(chunks) == 2
    assert chunks[0].metadata["section_id"] == "doctest::sec0"
    assert chunks[1].metadata["section_id"] == "doctest::sec1"


@pytest.mark.smoke
def test_min_emits_trailing_under_floor_chunk() -> None:
    """The last group may end up below the floor — we still emit it."""
    # Floor=10 tokens, max=12. First two paragraphs combine to 10. Trailing
    # third paragraph (5 tokens) gets emitted alone, under-floor.
    doc = build_document(
        sections_spec=[
            ("S1", [["A B C D E."], ["F G H I J."], ["K L M."]]),
        ],
    )
    chunks = ParentChildChunker(
        max_child_tokens=12,
        min_child_tokens=10,
        token_count=lambda t: max(1, len(t) // 2),  # ~10 tokens for 5-letter sentences
    ).chunk(doc)

    # Trailing single-paragraph chunk should still appear
    assert len(chunks) >= 2
    last_chunk_sentences = chunks[-1].sentence_ids
    assert "doctest::s2" in last_chunk_sentences
    assert_chunk_invariants(doc, chunks)


@pytest.mark.smoke
def test_min_merge_does_not_overflow_max() -> None:
    """A merged chunk must still respect max_child_tokens."""
    # 5 paragraphs × 1 sentence × 30 tokens each.  min=20, max=70.
    # Greedy fill: para1 (30) below max-overflow with para2 (30) → 60 ≤ 70 → keep.
    # Adding para3 (30) → 90 > 70 → flush 60. Start fresh with para3 (30).
    # Para4 (30) → 60 ≤ 70 → keep.  Para5 (30) → 90 > 70 → flush 60. Start with para5.
    # Trailing flush: para5 alone (30).
    doc = build_document(
        sections_spec=[
            ("S1", [["A."], ["B."], ["C."], ["D."], ["E."]]),
        ],
    )
    chunks = ParentChildChunker(
        max_child_tokens=70,
        min_child_tokens=20,
        token_count=lambda _t: 30,
    ).chunk(doc)

    # Every chunk's text-tokens must be <= max
    for ch in chunks:
        toks = sum(30 for _ in ch.sentence_ids)
        assert toks <= 70, f"chunk {ch.chunk_id} is {toks} tokens, exceeds max=70"

    assert_chunk_invariants(doc, chunks)


@pytest.mark.smoke
def test_metadata_paragraph_ids_includes_all_paragraphs() -> None:
    """Multi-paragraph chunks expose all touched paragraph IDs."""
    doc = build_document(
        sections_spec=[
            ("S1", [["A."], ["B."], ["C."]]),  # three tiny paras
        ],
    )
    chunks = ParentChildChunker(
        max_child_tokens=400,
        min_child_tokens=10,  # high enough to force merging
        token_count=lambda t: max(1, len(t) // 4),
    ).chunk(doc)

    assert len(chunks) == 1
    md = chunks[0].metadata
    # Backwards-compat: paragraph_id is the first paragraph touched
    assert md["paragraph_id"] == "doctest::para0"
    # New: paragraph_ids enumerates all of them in order
    assert md["paragraph_ids"] == ("doctest::para0", "doctest::para1", "doctest::para2")
    # Multi-paragraph chunks get trivial part numbering
    assert md["paragraph_part"] == 0
    assert md["paragraph_part_count"] == 1


@pytest.mark.smoke
def test_metadata_paragraph_ids_single_for_unmerged_chunks() -> None:
    """When a chunk maps to one paragraph, paragraph_ids has a single entry."""
    doc = build_document(
        sections_spec=[
            ("S1", [["This is a sentence.", "Another one here."]]),
        ],
    )
    chunks = ParentChildChunker().chunk(doc)
    assert len(chunks) == 1
    assert chunks[0].metadata["paragraph_ids"] == ("doctest::para0",)
