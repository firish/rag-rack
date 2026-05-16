"""Align a benchmark's gold passage text to sentence IDs in our parsed Document.

LitQA2 (and similar benchmarks) ship gold passages as raw text excerpts from
a source paper. Our pipeline stores parsed sentences with stable IDs. This
module bridges the two: given a gold passage and the parsed Document, return
the set of sentence IDs whose text overlaps with the passage.

Why this is non-trivial
-----------------------
Both texts describe the same physical passage but won't be byte-identical:
- Whitespace, line breaks, hyphenation differences
- Ligatures (fi → fi, fl → fl)
- Quote/dash characters (curly vs straight)
- Sentence-segmentation boundaries (Docling/wtpsplit may split sentences
  differently than where the gold passage starts/ends)
- Occasional OCR artifacts on older PDFs

Strategy
--------
1. Normalize both sides (lowercase, collapse whitespace, strip non-word chars).
2. For each parsed sentence, score how well it appears within the gold
   passage using ``rapidfuzz.fuzz.partial_ratio`` (returns 0-100).
3. Include sentences scoring above ``threshold`` (default 80).

``partial_ratio`` returns the best-aligned substring score, so for a long
gold passage and a shorter parsed sentence, it correctly identifies whether
the sentence appears (roughly) verbatim somewhere inside the passage.

Tunable
-------
- ``threshold`` of 80 catches near-verbatim matches with minor noise. Raise
  to ~90 for stricter alignment, lower to ~70 if many sentences should
  match but aren't being picked up.
- ``min_sentence_chars`` (default 25) filters out very short fragments
  ("Yes.", "Figure 2.") that would false-match against any longer passage.
"""

from __future__ import annotations

import re
from typing import Any

from verifiable_rag.models.document import Document


def align_passage_to_sentences(
    passage: str,
    document: Document,
    threshold: int = 80,
    min_sentence_chars: int = 25,
) -> set[str]:
    """Find sentence IDs in *document* whose text overlaps with *passage*.

    Uses fuzzy partial matching to handle whitespace, ligature, and
    sentence-boundary differences between the gold-annotation text source
    and our parser's output.

    Returns the (possibly empty) set of matching sentence IDs.
    """
    if not passage or not passage.strip():
        return set()

    try:
        from rapidfuzz import fuzz
    except ImportError as exc:
        raise ImportError(
            "rapidfuzz is required for passage alignment. Install with: pip install rapidfuzz"
        ) from exc

    norm_passage = _normalize(passage)
    if not norm_passage:
        return set()

    matched: set[str] = set()
    for sentence in document.sentences:
        norm_sent = _normalize(sentence.text)
        if len(norm_sent) < min_sentence_chars:
            continue

        # First: cheap exact substring check (catches the verbatim case fast)
        if norm_sent in norm_passage or norm_passage in norm_sent:
            matched.add(sentence.id)
            continue

        # Otherwise: fuzzy partial match. partial_ratio returns the best
        # score for the shorter string aligned within the longer one.
        score = fuzz.partial_ratio(norm_sent, norm_passage)
        if score >= threshold:
            matched.add(sentence.id)

    return matched


# --------------------------------------------------------------------------- #
# Internals
# --------------------------------------------------------------------------- #


_PUNCT_RE = re.compile(r"[^\w\s]")
_SPACE_RE = re.compile(r"\s+")

# Common ligature / smart-quote replacements seen in academic PDFs
_REPLACEMENTS: dict[str, str] = {
    "ﬀ": "ff",
    "ﬁ": "fi",
    "ﬂ": "fl",
    "ﬃ": "ffi",
    "ﬄ": "ffl",
    "‐": "-",  # hyphen
    "‑": "-",  # non-breaking hyphen
    "‒": "-",  # figure dash
    "–": "-",  # en dash
    "—": "-",  # em dash
    "‘": "'",  # left single
    "’": "'",  # right single
    "“": '"',  # left double
    "”": '"',  # right double
    " ": " ",  # non-breaking space
}


def _normalize(text: str) -> str:
    """Lowercase, expand ligatures/dashes, strip punctuation, collapse whitespace."""
    s = text
    for old, new in _REPLACEMENTS.items():
        s = s.replace(old, new)
    s = s.lower()
    s = _PUNCT_RE.sub(" ", s)
    s = _SPACE_RE.sub(" ", s).strip()
    return s


def alignment_summary(
    passage: str,
    document: Document,
    threshold: int = 80,
    min_sentence_chars: int = 25,
) -> dict[str, Any]:
    """Diagnostic helper: returns matched sentence IDs + raw scores for inspection."""
    try:
        from rapidfuzz import fuzz
    except ImportError as exc:
        raise ImportError("rapidfuzz is required") from exc

    norm_passage = _normalize(passage)
    scores: list[tuple[str, float]] = []
    for sentence in document.sentences:
        norm_sent = _normalize(sentence.text)
        if len(norm_sent) < min_sentence_chars:
            continue
        if norm_sent in norm_passage or norm_passage in norm_sent:
            scores.append((sentence.id, 100))
        else:
            scores.append((sentence.id, fuzz.partial_ratio(norm_sent, norm_passage)))

    matched = [(sid, score) for sid, score in scores if score >= threshold]
    return {
        "matched_count": len(matched),
        "matched_ids": [sid for sid, _ in matched],
        "top_5_by_score": sorted(scores, key=lambda x: x[1], reverse=True)[:5],
        "threshold": threshold,
    }
