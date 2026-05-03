"""Parser-test helpers.

The most important thing here is ``assert_span_invariants`` — every parser test
calls this to enforce the foundational rule from CLAUDE.md §6:
``doc.full_text[s.span.char_start:s.span.char_end] == s.text`` for every sentence.
If this ever fails, downstream citations are silently corrupt.
"""
from __future__ import annotations

from verifiable_rag.models.document import Document
from verifiable_rag.parsers._sentence_splitter import SentenceSpan


def assert_span_invariants(doc: Document) -> None:
    """Assert every span-tracking guarantee that downstream layers rely on."""
    # ---- page_breaks ------------------------------------------------------
    assert doc.page_breaks, f"Document {doc.doc_id!r} has no page_breaks"
    assert doc.page_breaks[0] == 0, (
        f"page_breaks[0] must be 0, got {doc.page_breaks[0]} for {doc.doc_id!r}"
    )
    assert doc.page_breaks == sorted(doc.page_breaks), (
        f"page_breaks not sorted: {doc.page_breaks}"
    )

    # ---- sentence-level: doc_id, ordering, span/text round-trip ----------
    for sent in doc.sentences:
        assert sent.span.doc_id == doc.doc_id, (
            f"Sentence {sent.id!r} carries span.doc_id {sent.span.doc_id!r} "
            f"but document is {doc.doc_id!r}"
        )
        assert sent.span.char_end > sent.span.char_start, (
            f"Sentence {sent.id!r} has empty/inverted span: {sent.span}"
        )
        if doc.full_text is not None:
            actual = doc.full_text[sent.span.char_start : sent.span.char_end]
            assert actual == sent.text, (
                f"Span/text mismatch for {sent.id!r}:\n"
                f"  span      = {sent.span}\n"
                f"  expected  = {sent.text!r}\n"
                f"  full_text = {actual!r}"
            )
        # Sentence must map to a valid page range
        first_page, last_page = doc.pages_for_span(sent.span)
        assert 0 <= first_page <= last_page < doc.num_pages, (
            f"Sentence {sent.id!r} maps to invalid pages "
            f"[{first_page}, {last_page}] (num_pages={doc.num_pages})"
        )

    # ---- chunk-level: bounding spans contain their sentence spans --------
    for para in doc.paragraphs:
        sent_starts = [s.span.char_start for s in para.sentences]
        sent_ends = [s.span.char_end for s in para.sentences]
        assert para.span.char_start <= min(sent_starts), (
            f"Paragraph {para.id!r} span starts after its first sentence"
        )
        assert para.span.char_end >= max(sent_ends), (
            f"Paragraph {para.id!r} span ends before its last sentence"
        )


# --------------------------------------------------------------------------- #
# Lightweight stand-in for SentenceSplitter — splits on ". " + final period.
# Lets us test the parser's structural logic without downloading the wtpsplit
# model or requiring an internet connection.
# --------------------------------------------------------------------------- #

class SimpleSplitter:
    """Period-based sentence splitter.  Good enough to drive parser tests."""

    def split_with_offsets(self, text: str) -> list[SentenceSpan]:
        result: list[SentenceSpan] = []
        cursor = 0
        n = len(text)
        while cursor < n:
            # Skip leading whitespace
            while cursor < n and text[cursor].isspace():
                cursor += 1
            if cursor >= n:
                break
            # Find next sentence-ending period followed by space or end
            i = cursor
            while i < n:
                if text[i] == "." and (i + 1 == n or text[i + 1].isspace()):
                    i += 1  # include the period
                    break
                i += 1
            else:
                i = n
            sent_text = text[cursor:i]
            if sent_text.strip():
                result.append(SentenceSpan(text=sent_text, start=cursor, end=i))
            cursor = i
        return result
