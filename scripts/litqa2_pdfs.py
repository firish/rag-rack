"""LitQA2 PDF helpers — list DOIs and import manually-fetched PDFs.

Usage:
    # All 199 DOIs, one per line
    python scripts/litqa2_pdfs.py list

    # Only DOIs the auto-fetcher hasn't gotten yet
    python scripts/litqa2_pdfs.py list --failed

    # Markdown table with status, source, title (easier to skim)
    python scripts/litqa2_pdfs.py list --table

    # Import a manually-downloaded PDF into the cache (auto-computes the
    # right cache filename from the DOI)
    python scripts/litqa2_pdfs.py import path/to/paper.pdf 10.1126/science.abc1234

    # Refresh the index after importing a batch (re-scans cache dir)
    python scripts/litqa2_pdfs.py reindex
"""

from __future__ import annotations

import argparse
import json
import shutil
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from huggingface_hub import hf_hub_download

from verifiable_rag.eval.datasets._pdf_fetcher import _normalize_doi

CACHE_DIR = Path(".verifiable_rag_cache/litqa2_pdfs")
INDEX_PATH = CACHE_DIR / "_index.json"


def _load_dataset() -> list[dict[str, str | bool]]:
    """Load the 199 LitQA2 rows from the cached HuggingFace parquet."""
    import pandas as pd  # type: ignore[import-untyped]

    parquet = hf_hub_download(
        repo_id="futurehouse/lab-bench",
        filename="LitQA2/train-00000-of-00001.parquet",
        repo_type="dataset",
    )
    df = pd.read_parquet(parquet)
    out = []
    for _, row in df.iterrows():
        sources_field = row["sources"]
        doi = sources_field[0] if hasattr(sources_field, "__iter__") else sources_field
        out.append(
            {
                "id": str(row["id"]),
                "doi": str(doi),
                "is_opensource": bool(row["is_opensource"]),
                "title_hint": (str(row["question"])[:80] + "...")
                if len(str(row["question"])) > 80
                else str(row["question"]),
            }
        )
    return out


def _load_index() -> dict[str, dict[str, object]]:
    if not INDEX_PATH.exists():
        return {}
    return json.loads(INDEX_PATH.read_text())


def cmd_list(args: argparse.Namespace) -> int:
    dataset = _load_dataset()
    index = _load_index()

    rows = []
    for row in dataset:
        entry = index.get(row["id"], {}) or {}
        path = entry.get("path")
        rows.append(
            {
                **row,
                "fetched": bool(path),
                "source": entry.get("source"),
            }
        )

    if args.failed:
        rows = [r for r in rows if not r["fetched"]]

    if args.table:
        print(f"| {'is_OS':<5} | {'fetched':<7} | {'source':<22} | {'doi':<60} | question |")
        print(f"|{'-' * 7}|{'-' * 9}|{'-' * 24}|{'-' * 62}|----------|")
        for r in rows:
            mark = "T" if r["is_opensource"] else "F"
            fetched = "yes" if r["fetched"] else "no"
            src = r["source"] or "-"
            print(f"| {mark:<5} | {fetched:<7} | {src:<22} | {r['doi']:<60} | {r['title_hint']} |")
    else:
        # Plain DOI per line — easy to pipe to xargs / cat into a script
        for r in rows:
            print(r["doi"])

    return 0


def cmd_import(args: argparse.Namespace) -> int:
    src = Path(args.pdf)
    if not src.exists():
        print(f"PDF not found: {src}", file=sys.stderr)
        return 1
    if src.read_bytes()[:5] != b"%PDF-":
        print(f"WARNING: {src} doesn't start with %PDF- magic", file=sys.stderr)
        if not args.force:
            print("  use --force to import anyway", file=sys.stderr)
            return 1

    norm = _normalize_doi(args.doi)
    if not norm:
        print(f"Invalid DOI: {args.doi}", file=sys.stderr)
        return 1

    import hashlib

    digest = hashlib.sha256(norm.encode("utf-8")).hexdigest()[:16]
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    dest = CACHE_DIR / f"{digest}.pdf"

    if dest.exists() and not args.force:
        print(f"Already cached: {dest} (use --force to overwrite)", file=sys.stderr)
        return 1

    shutil.copy(src, dest)
    print(f"Imported {src} -> {dest} (DOI: {norm})")
    print("  Run `python scripts/litqa2_pdfs.py reindex` to update _index.json")
    return 0


def cmd_reindex(args: argparse.Namespace) -> int:
    """Re-scan the cache dir and rewrite _index.json to reflect what's there.

    Also re-computes the gold key-passage → sentence_id alignment for any
    paper that has a PDF cached. Pass ``--no-align`` to skip alignment
    (much faster — only the path/source bits get refreshed).
    """
    import hashlib

    do_align = not args.no_align
    parser = None
    align_passage_to_sentences = None
    if do_align:
        from verifiable_rag.eval.datasets._passage_aligner import (  # noqa: F401
            align_passage_to_sentences as _aligner,
        )
        from verifiable_rag.parsers import CachingParser, DoclingParser

        align_passage_to_sentences = _aligner
        parser = CachingParser(DoclingParser())

    dataset = _load_dataset_with_passages()
    existing = _load_index()

    new_index: dict[str, dict[str, object]] = {}
    new_hits = 0
    aligned_with_gold = 0
    for row in dataset:
        norm = _normalize_doi(row["doi"])
        digest = hashlib.sha256(norm.encode("utf-8")).hexdigest()[:16]
        cache_path = CACHE_DIR / f"{digest}.pdf"
        prior = existing.get(row["id"], {}) or {}

        if cache_path.exists() and cache_path.stat().st_size > 1024:
            entry: dict[str, object] = {
                "doi": norm,
                "is_opensource": row["is_opensource"],
                "path": str(cache_path),
                "source": prior.get("source") or "manual",
                "error": None,
            }
            new_hits += 1

            # Run/refresh alignment unless caller opted out
            key_passage_sentence_ids: list[str] = []
            align_error: str | None = None
            if do_align and parser is not None and align_passage_to_sentences is not None:
                key_passage = str(row.get("key_passage", "") or "")
                if key_passage.strip():
                    try:
                        document = parser.parse(cache_path)
                        matched = align_passage_to_sentences(key_passage, document)
                        key_passage_sentence_ids = sorted(matched)
                        if key_passage_sentence_ids:
                            aligned_with_gold += 1
                    except Exception as exc:  # noqa: BLE001
                        align_error = f"{type(exc).__name__}: {exc}"
                else:
                    align_error = "no key_passage in dataset row"
            else:
                # Preserve any previously computed alignment
                key_passage_sentence_ids = list(prior.get("key_passage_sentence_ids") or [])
                align_error = prior.get("align_error")  # type: ignore[assignment]

            entry["key_passage_sentence_ids"] = key_passage_sentence_ids
            entry["align_error"] = align_error
            new_index[row["id"]] = entry
        else:
            new_index[row["id"]] = {
                "doi": norm,
                "is_opensource": row["is_opensource"],
                "path": None,
                "source": prior.get("source"),
                "error": prior.get("error") or "pdf not in cache",
                "key_passage_sentence_ids": [],
                "align_error": None,
            }

    INDEX_PATH.parent.mkdir(parents=True, exist_ok=True)
    INDEX_PATH.write_text(json.dumps(new_index, indent=2))
    total = len(new_index)
    print(f"Reindexed: {new_hits}/{total} have PDFs ({100 * new_hits / total:.1f}%)")
    if do_align:
        print(f"           {aligned_with_gold} aligned with gold key-passage sentences")
    print(f"  Wrote: {INDEX_PATH}")
    return 0


def _load_dataset_with_passages() -> list[dict[str, str | bool]]:
    """Like ``_load_dataset`` but also surfaces the ``key-passage`` column."""
    import pandas as pd  # type: ignore[import-untyped]

    parquet = hf_hub_download(
        repo_id="futurehouse/lab-bench",
        filename="LitQA2/train-00000-of-00001.parquet",
        repo_type="dataset",
    )
    df = pd.read_parquet(parquet)
    out = []
    for _, row in df.iterrows():
        sources_field = row["sources"]
        doi = sources_field[0] if hasattr(sources_field, "__iter__") else sources_field
        out.append(
            {
                "id": str(row["id"]),
                "doi": str(doi),
                "is_opensource": bool(row["is_opensource"]),
                "key_passage": str(row.get("key-passage", "") or ""),
            }
        )
    return out


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="litqa2_pdfs.py")
    sub = p.add_subparsers(dest="cmd", required=True)

    list_p = sub.add_parser("list", help="List DOIs (all or failed-only)")
    list_p.add_argument("--failed", action="store_true", help="Only show un-fetched DOIs")
    list_p.add_argument("--table", action="store_true", help="Print a markdown table")
    list_p.set_defaults(fn=cmd_list)

    imp_p = sub.add_parser("import", help="Drop a manually-fetched PDF into the cache")
    imp_p.add_argument("pdf", help="Path to the PDF file")
    imp_p.add_argument("doi", help="DOI of the paper (with or without https://doi.org/)")
    imp_p.add_argument("--force", action="store_true", help="Overwrite if already cached")
    imp_p.set_defaults(fn=cmd_import)

    reidx_p = sub.add_parser("reindex", help="Refresh _index.json based on cache contents")
    reidx_p.add_argument(
        "--no-align",
        action="store_true",
        help="Skip the key-passage→sentence_id alignment (much faster)",
    )
    reidx_p.set_defaults(fn=cmd_reindex)

    return p


if __name__ == "__main__":
    parser = build_parser()
    args = parser.parse_args()
    sys.exit(args.fn(args))
