"""Fetch all 199 LitQA2 PDFs into the local cache + align gold passages.

Two-stage script:
1. Fetch each paper's PDF via the multi-fallback PdfFetcher (Unpaywall,
   OpenAlex, Semantic Scholar, CORE, PMC/Europe PMC, bioRxiv, arXiv,
   direct DOI scrape, and Playwright as the second-pass browser fallback).
2. For each successfully fetched paper, parse it (CachingParser) and
   align LitQA2's ``key-passage`` field to the parsed sentence IDs.
   The matching set is stored in the index so the benchmark adapter can
   surface real citation gold (not vacuous empty sets).

Output:
- PDFs in `.verifiable_rag_cache/litqa2_pdfs/<doi-hash>.pdf`
- An index JSON at `.verifiable_rag_cache/litqa2_pdfs/_index.json`
  mapping each question_id → {doi, path, source, key_passage_sentence_ids}.

Run from repo root:
    set -a && source .env && set +a
    python scripts/fetch_litqa2.py
"""

from __future__ import annotations

import json
import logging
import sys
import time
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

import pandas as pd
from huggingface_hub import hf_hub_download

from verifiable_rag.eval.datasets._passage_aligner import align_passage_to_sentences
from verifiable_rag.eval.datasets._pdf_fetcher import PdfFetcher
from verifiable_rag.parsers import CachingParser, DoclingParser

logger = logging.getLogger(__name__)

CACHE_DIR = Path(".verifiable_rag_cache/litqa2_pdfs")
INDEX_PATH = CACHE_DIR / "_index.json"


def _align_one(
    parser: CachingParser,
    pdf_path: Path,
    key_passage: str,
) -> tuple[list[str], str | None]:
    """Parse a PDF and align its sentences to the gold key-passage.

    Returns (matched_sentence_ids, error_message).
    Errors are silenced so the rest of the fetch/index can continue.
    """
    if not key_passage or not key_passage.strip():
        return [], "no key_passage in dataset row"
    try:
        document = parser.parse(pdf_path)
    except Exception as exc:  # noqa: BLE001
        return [], f"parse failed: {type(exc).__name__}: {exc}"
    try:
        matched = align_passage_to_sentences(key_passage, document)
        return sorted(matched), None
    except Exception as exc:  # noqa: BLE001
        return [], f"align failed: {type(exc).__name__}: {exc}"


def main() -> None:
    print("Loading LitQA2 dataset...")
    parquet = hf_hub_download(
        repo_id="futurehouse/lab-bench",
        filename="LitQA2/train-00000-of-00001.parquet",
        repo_type="dataset",
    )
    df = pd.read_parquet(parquet)
    print(f"  {len(df)} questions, {df.is_opensource.sum()} marked opensource")

    sources_count: Counter[str] = Counter()
    index: dict[str, dict[str, object]] = {}
    parser = CachingParser(DoclingParser())

    aligned_with_gold = 0
    aligned_empty = 0

    with PdfFetcher(cache_dir=CACHE_DIR) as fetcher:
        for i, (_, row) in enumerate(df.iterrows(), start=1):
            sources_field = row["sources"]
            doi = sources_field[0] if hasattr(sources_field, "__iter__") else sources_field
            doi = str(doi)
            print(f"[{i:>3}/{len(df)}] {doi}")
            res = fetcher.fetch(doi)
            src = res.source or "FAIL"
            sources_count[src] += 1

            # Stage 2: align the gold passage to parsed sentence IDs (only when
            # we have a PDF). DocumentCache makes the parse cheap on re-runs.
            key_passage_sentence_ids: list[str] = []
            align_error: str | None = None
            if res.path:
                key_passage = str(row.get("key-passage", "") or "")
                key_passage_sentence_ids, align_error = _align_one(parser, res.path, key_passage)
                if key_passage_sentence_ids:
                    aligned_with_gold += 1
                else:
                    aligned_empty += 1
                    if align_error:
                        print(f"      align: {align_error}")

            index[row["id"]] = {
                "doi": doi,
                "is_opensource": bool(row["is_opensource"]),
                "path": str(res.path) if res.path else None,
                "source": res.source,
                "error": res.error,
                "key_passage_sentence_ids": key_passage_sentence_ids,
                "align_error": align_error,
            }
            # Stream-save the index so a crash mid-run doesn't lose progress
            CACHE_DIR.mkdir(parents=True, exist_ok=True)
            INDEX_PATH.write_text(json.dumps(index, indent=2))
            time.sleep(0.5)  # politeness between requests

    print()
    print("=" * 60)
    print(f"COMPLETE — {len(df)} attempted")
    hits = sum(1 for v in index.values() if v["path"])
    print(f"  PDFs:                    {hits}/{len(df)} = {100 * hits / len(df):.1f}%")
    print(f"  With non-empty gold IDs: {aligned_with_gold}")
    print(f"  Fetched but no gold IDs: {aligned_empty}")
    print(f"  Index written to:        {INDEX_PATH}")
    print()
    print("Source breakdown:")
    for s, n in sources_count.most_common():
        print(f"  {s:<25} {n}")


if __name__ == "__main__":
    main()
