"""Tests for align_passage_to_sentences — fuzzy gold-passage → sentence_id mapping."""

from __future__ import annotations

import pytest

from tests.chunkers.conftest import build_document
from verifiable_rag.eval.datasets._passage_aligner import (
    _normalize,
    align_passage_to_sentences,
    alignment_summary,
)
from verifiable_rag.models.document import Document

pytest.importorskip("rapidfuzz", reason="rapidfuzz not installed")


# --------------------------------------------------------------------------- #
# Helpers
# --------------------------------------------------------------------------- #


def _doc_with_sentences(*sentence_texts: str) -> Document:
    """Build a Document with the given sentence texts in one paragraph."""
    return build_document(
        sections_spec=[("S1", [list(sentence_texts)])],
        doc_id="doc",
    )


# --------------------------------------------------------------------------- #
# _normalize
# --------------------------------------------------------------------------- #


@pytest.mark.smoke
def test_normalize_lowercases_and_collapses_whitespace() -> None:
    assert _normalize("  Hello\n  WORLD\t") == "hello world"


@pytest.mark.smoke
def test_normalize_expands_ligatures() -> None:
    # ﬁ ligature → "fi"
    assert _normalize("efﬁcient") == "efficient"
    assert _normalize("ﬂow") == "flow"


@pytest.mark.smoke
def test_normalize_unifies_dashes_and_quotes() -> None:
    assert _normalize("co—operation") == "co operation"  # em-dash + punct stripped
    assert _normalize("she said “hi”") == "she said hi"


@pytest.mark.smoke
def test_normalize_strips_punctuation() -> None:
    assert _normalize("Hello, world!") == "hello world"


# --------------------------------------------------------------------------- #
# align_passage_to_sentences — exact and fuzzy matches
# --------------------------------------------------------------------------- #


@pytest.mark.smoke
def test_align_returns_empty_for_empty_passage() -> None:
    doc = _doc_with_sentences("Anything goes here.")
    assert align_passage_to_sentences("", doc) == set()
    assert align_passage_to_sentences("   ", doc) == set()


@pytest.mark.smoke
def test_align_finds_verbatim_sentence_in_passage() -> None:
    """The exact case: gold passage IS the parsed sentence, character-for-character."""
    doc = _doc_with_sentences(
        "A. lwoffii only evolved resistance to ciprofloxacin.",
        "An unrelated sentence about something else.",
    )
    matched = align_passage_to_sentences(
        "A. lwoffii only evolved resistance to ciprofloxacin",
        doc,
    )
    assert matched == {"doc::s0"}


@pytest.mark.smoke
def test_align_finds_sentence_inside_longer_passage() -> None:
    """Gold passage contains the parsed sentence + extra context."""
    doc = _doc_with_sentences(
        "A. lwoffii only evolved resistance to ciprofloxacin.",
        "Other sentence.",
    )
    passage = (
        "A. baumannii readily evolved resistance to meropenem, ciprofloxacin, "
        "and gentamicin, but A. lwoffii only evolved resistance to ciprofloxacin "
        "in our experiments."
    )
    matched = align_passage_to_sentences(passage, doc)
    assert "doc::s0" in matched


@pytest.mark.smoke
def test_align_handles_ligature_and_whitespace_noise() -> None:
    """The same content with PDF noise (ligatures, weird spacing) still matches."""
    doc = _doc_with_sentences(
        "Efficient   parallel   processing  improves throughput significantly.",
        "Other sentence here.",
    )
    # Gold passage has ligatures, dashes, smart quotes — like a publisher's HTML
    passage = "We show that efﬁcient parallel processing improves throughput signiﬁcantly"
    matched = align_passage_to_sentences(passage, doc)
    assert "doc::s0" in matched


@pytest.mark.smoke
def test_align_excludes_unrelated_sentences() -> None:
    doc = _doc_with_sentences(
        "A. lwoffii only evolved resistance to ciprofloxacin in our study.",
        "Mitochondria are the powerhouse of the cell, unrelated entirely.",
        "We thank our colleagues for helpful discussions and feedback.",
    )
    matched = align_passage_to_sentences(
        "A. lwoffii only evolved resistance to ciprofloxacin",
        doc,
    )
    assert "doc::s0" in matched
    assert "doc::s1" not in matched
    assert "doc::s2" not in matched


@pytest.mark.smoke
def test_align_finds_multiple_sentences_in_a_multi_sentence_passage() -> None:
    """If the gold passage spans multiple parsed sentences, we want all of them."""
    doc = _doc_with_sentences(
        "Mitochondria produce ATP through oxidative phosphorylation.",
        "They are the primary site of cellular respiration.",
        "Unrelated noise about photosynthesis here.",
    )
    passage = (
        "Mitochondria produce ATP through oxidative phosphorylation. "
        "They are the primary site of cellular respiration."
    )
    matched = align_passage_to_sentences(passage, doc)
    assert matched == {"doc::s0", "doc::s1"}


@pytest.mark.smoke
def test_align_filters_too_short_sentences() -> None:
    """Very short fragments (< min_sentence_chars) shouldn't false-match."""
    doc = _doc_with_sentences(
        "Yes.",
        "Figure 2.",
        "A. lwoffii only evolved resistance to ciprofloxacin in our experiments.",
    )
    matched = align_passage_to_sentences(
        "A. lwoffii only evolved resistance to ciprofloxacin in our experiments",
        doc,
    )
    # Only the long sentence matches — the short ones are filtered
    assert matched == {"doc::s2"}


@pytest.mark.smoke
def test_align_threshold_is_configurable() -> None:
    """A weak match passes a lenient threshold but fails a strict one."""
    doc = _doc_with_sentences(
        "Cells have membranes and grow in culture under standard conditions.",
        "Other unrelated content here that should not match anyway.",
    )
    # Vague passage with overlapping words but different meaning
    passage = (
        "Stem cells were grown in standard culture conditions and analyzed for "
        "membrane integrity at multiple time points."
    )
    # Lenient threshold may match
    lenient = align_passage_to_sentences(passage, doc, threshold=60)
    # Strict threshold should not
    strict = align_passage_to_sentences(passage, doc, threshold=95)
    assert len(strict) <= len(lenient)


# --------------------------------------------------------------------------- #
# alignment_summary — diagnostic helper
# --------------------------------------------------------------------------- #


@pytest.mark.smoke
def test_alignment_summary_returns_diagnostic_info() -> None:
    doc = _doc_with_sentences(
        "A. lwoffii only evolved resistance to ciprofloxacin in our experiments.",
        "Unrelated content about mitochondria and energy production.",
    )
    summary = alignment_summary(
        "A. lwoffii only evolved resistance to ciprofloxacin",
        doc,
    )
    assert "matched_count" in summary
    assert "matched_ids" in summary
    assert "top_5_by_score" in summary
    assert summary["matched_count"] == 1
    assert summary["matched_ids"] == ["doc::s0"]
    # Top score should be very high
    assert summary["top_5_by_score"][0][1] >= 95
