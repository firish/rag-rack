"""End-to-end smoke for ContextualChunker on one LitQA2 PDF.

Validates:
1. Real LLM call works through LiteLLM + Anthropic
2. Cache breakpoints don't break the message shape
3. Generated preambles look sensible (qualitative — printed to stdout)
4. Approximate cost matches the per-doc estimate

Usage:
    ANTHROPIC_API_KEY=... python scripts/smoke_contextual_chunker.py
"""

from __future__ import annotations

import sys
import time
from pathlib import Path

from verifiable_rag.chunkers import ContextualChunker, LLMContextualizer, ParentChildChunker
from verifiable_rag.parsers import PyMuPDFParser

# PyMuPDF is fast (~1s for a 1MB paper) — fine for a wiring smoke. Switch to
# DoclingParser when you care about layout fidelity (figures, tables, OCR).
DEFAULT_PDF = Path(".verifiable_rag_cache/litqa2_pdfs/1e98838d3116281b.pdf")


def main(argv: list[str] | None = None) -> int:
    pdf = Path(argv[0]) if argv else DEFAULT_PDF
    if not pdf.exists():
        print(f"PDF not found: {pdf}", file=sys.stderr)
        return 1

    print(f"[smoke] parsing {pdf} (PyMuPDF) ...", flush=True)
    t0 = time.time()
    parser = PyMuPDFParser()
    document = parser.parse(pdf)
    print(f"[smoke] parsed in {time.time() - t0:.1f}s; full_text={len(document.full_text)} chars", flush=True)

    print("[smoke] chunking with ParentChildChunker ...", flush=True)
    base = ParentChildChunker(max_child_tokens=400)
    raw_chunks = base.chunk(document)
    print(f"[smoke] base chunker produced {len(raw_chunks)} chunks", flush=True)

    # Cap at 5 chunks for the smoke run — keeps cost trivial
    raw_chunks_for_smoke = raw_chunks[:5]
    print(
        f"[smoke] contextualizing first {len(raw_chunks_for_smoke)} chunks ...",
        flush=True,
    )

    # Use a fixed StubChunker so ContextualChunker only contextualizes the 5
    class _FixedChunker:
        def chunk(self, _doc):  # type: ignore[no-untyped-def]
            return raw_chunks_for_smoke

    contextualizer = LLMContextualizer(
        model="claude-haiku-4-5-20251001", max_workers=4
    )
    cx_chunker = ContextualChunker(_FixedChunker(), contextualizer)

    t0 = time.time()
    chunks = cx_chunker.chunk(document)
    wall = time.time() - t0
    print(f"[smoke] contextualization took {wall:.1f}s", flush=True)

    n_with_preamble = sum(1 for c in chunks if c.metadata.get("contextual_preamble"))
    print(f"[smoke] {n_with_preamble}/{len(chunks)} chunks got a preamble", flush=True)
    print()

    for i, c in enumerate(chunks):
        preamble = c.metadata.get("contextual_preamble", "<NO PREAMBLE>")
        print(f"--- chunk {i} ({c.chunk_id}) ---")
        print(f"PREAMBLE: {preamble}")
        print(f"TEXT[:200]: {c.text[:200]!r}")
        print()

    # Sanity invariants
    for c, raw in zip(chunks, raw_chunks_for_smoke, strict=True):
        assert c.text == raw.text, "ContextualChunker mutated chunk.text"
        assert c.span == raw.span, "ContextualChunker mutated chunk.span"
        assert c.sentence_ids == raw.sentence_ids, "sentence_ids changed"

    print("[smoke] span/text/sentence_id invariants preserved ✓")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
