"""Fetch the canonical ALCE eval data into the local cache.

ALCE (Princeton NLP, EMNLP 2023) is THE citation-quality benchmark for RAG:
its primary metrics are ``citation_recall`` and ``citation_precision`` over
hand-annotated supporting passages, which directly map onto what
verifiable-rag is built to measure.

Three sub-benchmarks bundled in the canonical archive:
  - ASQA      (~948 factoid Qs with ambiguity)
  - QAMPARI   (~1k multi-hop factoid Qs)
  - ELI5      (~1k long-form Qs)

The HF dataset ``princeton-nlp/ALCE-data`` ships a single ``ALCE-data.tar``
that we download once and extract under ``.verifiable_rag_cache/alce/``.
Each eval file inside the tarball already carries top-100 retrieved
passages so evaluation is self-contained — no separate Wikipedia/SPLADE
corpus download required. Swapping in our own retrieval over the source
corpora is a follow-on; not blocked by this loader.
"""
from __future__ import annotations

import sys
import tarfile
from pathlib import Path

from huggingface_hub import hf_hub_download

ALCE_CACHE = Path(".verifiable_rag_cache/alce")
ALCE_REPO_ID = "princeton-nlp/ALCE-data"
ALCE_TARBALL = "ALCE-data.tar"


def fetch_alce() -> Path:
    """Download + extract the ALCE tarball. Returns the extraction root.

    Idempotent: if the tarball is already cached AND the extracted tree
    exists, returns immediately without re-downloading or re-extracting.
    """
    ALCE_CACHE.mkdir(parents=True, exist_ok=True)
    marker = ALCE_CACHE / ".extracted"

    print(f"[alce] downloading {ALCE_TARBALL} (this is the only network step)...", flush=True)
    tar_path = Path(hf_hub_download(
        repo_id=ALCE_REPO_ID,
        filename=ALCE_TARBALL,
        repo_type="dataset",
    ))
    size_mb = tar_path.stat().st_size / 1024 / 1024
    print(f"[alce]   tarball = {size_mb:.1f} MB at {tar_path}", flush=True)

    if marker.exists():
        print(f"[alce] already extracted at {ALCE_CACHE}; skipping untar.")
        return ALCE_CACHE

    print(f"[alce] extracting to {ALCE_CACHE}...", flush=True)
    with tarfile.open(tar_path, "r") as tf:
        # `data="data"` filter blocks absolute paths and ``..`` traversal
        tf.extractall(path=ALCE_CACHE, filter="data")
    marker.touch()
    print(f"[alce] extracted.", flush=True)
    return ALCE_CACHE


def main() -> int:
    try:
        root = fetch_alce()
    except Exception as exc:  # noqa: BLE001
        print(f"[alce] FAILED: {type(exc).__name__}: {exc}", file=sys.stderr)
        return 1

    # Surface what we got so the user knows what's available.
    print()
    print("[alce] contents:")
    for path in sorted(root.rglob("*")):
        if path.is_file() and not path.name.startswith("."):
            rel = path.relative_to(root)
            size_mb = path.stat().st_size / 1024 / 1024
            print(f"  {rel}  ({size_mb:.1f} MB)")
    print()
    print(f"[alce] done. Data ready at {root}/")
    return 0


if __name__ == "__main__":
    sys.exit(main())
