"""Quick sanity-check for DoclingParser on a real PDF.

Usage:
    python examples/inspect_parser.py <path/to/file.pdf>

Prints a structured summary: page count, section/paragraph/sentence counts,
span invariant check, and the first 3 sentences with their page assignments.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from verifiable_rag.parsers import CachingParser, DoclingParser


def main(pdf_path: Path) -> None:
    print(f"\nParsing: {pdf_path}")
    print("-" * 60)

    parser = CachingParser(DoclingParser())
    doc = parser.parse(pdf_path)

    # --- top-level stats ---
    all_sents = doc.sentences
    print(f"doc_id       : {doc.doc_id}")
    print(f"pages        : {doc.num_pages}")
    print(f"sections     : {len(doc.sections)}")
    print(f"paragraphs   : {len(doc.paragraphs)}")
    print(f"sentences    : {len(all_sents)}")
    print(f"full_text len: {len(doc.full_text):,} chars")

    # --- span invariant check ---
    print("\nSpan invariant check (full_text[start:end] == sentence.text):")
    failures = [
        s for s in all_sents
        if doc.full_text[s.span.char_start:s.span.char_end] != s.text
    ]
    if failures:
        print(f"  FAILED on {len(failures)} sentence(s)!")
        for s in failures[:3]:
            print(f"    id={s.id}")
            print(f"    stored : {s.text!r}")
            print(f"    in text: {doc.full_text[s.span.char_start:s.span.char_end]!r}")
    else:
        print(f"  OK — all {len(all_sents)} sentences round-trip correctly")

    # --- section overview ---
    print("\nSections:")
    for i, sec in enumerate(doc.sections):
        title = sec.title or "(no title)"
        print(f"  [{i}] {title!r}  — {len(sec.paragraphs)} para(s), {len(sec.sentences)} sent(s)")

    # --- first 5 sentences with page info ---
    print("\nFirst 5 sentences:")
    for sent in all_sents[:5]:
        first_page, last_page = doc.pages_for_span(sent.span)
        page_str = f"p{first_page + 1}" if first_page == last_page else f"p{first_page + 1}–{last_page + 1}"
        bbox_count = len(sent.span.bboxes)
        print(f"  [{page_str}] ({bbox_count} bbox(es)) {sent.text[:80]!r}")

    # --- cross-page sentences (if any) ---
    cross = [s for s in all_sents if len(s.span.bboxes) == 0]
    if cross:
        print(f"\nCross-page sentences (bboxes=(), char offsets still valid): {len(cross)}")
        for s in cross[:2]:
            first, last = doc.pages_for_span(s.span)
            print(f"  p{first + 1}–{last + 1}: {s.text[:60]!r}")
    else:
        print("\nNo cross-page sentences detected.")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        default = Path("tests/parsers/fixtures/sample.pdf")
        if default.exists():
            main(default)
        else:
            print("Usage: python examples/inspect_parser.py <path/to/file.pdf>")
            sys.exit(1)
    else:
        main(Path(sys.argv[1]))
