"""Fetch the small faithfulness/hallucination benchmark datasets locally.

These are all tiny (~10-30 MB each), so we batch them into one fetch
rather than per-benchmark scripts. Each lands under its own subdir of
``.verifiable_rag_cache/`` so loader code stays self-contained.

  RAGTruth     — word-level hallucination annotations across QA / d2t /
                 summarization. 18K annotated LLM responses. *The*
                 canonical hallucination-detection benchmark.
                 Repo: wandb/RAGTruth-processed (parquet, ~25 MB)

  HaluBench    — binary "is this hallucinated?" labels across QA,
                 dialogue, summarization, general. 35K examples.
                 Repo: PatronusAI/HaluBench (~30 MB)

  FaithBench   — sentence-level faithfulness labels in summarization,
                 ~1K examples × 10 LLMs. Newer (NAACL 2025).
                 Repo: vectara/FaithBench (~5-10 MB)
"""
from __future__ import annotations

import sys
from pathlib import Path

from huggingface_hub import hf_hub_download, list_repo_files

CACHE_ROOT = Path(".verifiable_rag_cache")

BENCHES: tuple[tuple[str, str, str], ...] = (
    # (cache_subdir, hf_repo_id, repo_type)
    ("ragtruth", "wandb/RAGTruth-processed", "dataset"),
    ("halubench", "PatronusAI/HaluBench", "dataset"),
    ("faithbench", "vectara/FaithBench", "dataset"),
)


def _fetch_repo(subdir: str, repo_id: str, repo_type: str) -> Path:
    target_dir = CACHE_ROOT / subdir
    target_dir.mkdir(parents=True, exist_ok=True)
    print(f"\n[{subdir}] fetching {repo_id} ({repo_type})...", flush=True)
    try:
        files = list_repo_files(repo_id, repo_type=repo_type)
    except Exception as exc:  # noqa: BLE001
        print(f"[{subdir}] FAILED to list files: {type(exc).__name__}: {exc}", flush=True)
        return target_dir
    # Skip gitattributes / readmes etc., grab data files
    keep = [f for f in files if not f.startswith(".") and f != "README.md"]
    for fname in keep:
        try:
            local = hf_hub_download(repo_id=repo_id, filename=fname, repo_type=repo_type)
        except Exception as exc:  # noqa: BLE001
            print(f"  {fname}: FAILED ({type(exc).__name__}: {exc})", flush=True)
            continue
        size_mb = Path(local).stat().st_size / 1024 / 1024
        print(f"  {fname:<60s} {size_mb:>7.2f} MB", flush=True)
    return target_dir


def main() -> int:
    CACHE_ROOT.mkdir(parents=True, exist_ok=True)
    for subdir, repo, repo_type in BENCHES:
        _fetch_repo(subdir, repo, repo_type)
    print()
    print(f"[done] all three faithfulness benches cached under {CACHE_ROOT}/")
    return 0


if __name__ == "__main__":
    sys.exit(main())
