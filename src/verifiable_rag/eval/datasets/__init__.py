"""Benchmark dataset loaders.

Datasets are downloaded on first use and cached locally.
Never commit raw benchmark data — add benchmarks/data/ to .gitignore.

Loaders to implement in Phase 0:
  - LitQA2    (FutureHouse scientific Q&A)
  - RAGTruth  (hallucination annotations)
  - HaluBench (faithfulness eval)
"""
from __future__ import annotations


def load_litqa2(cache_dir: str = "benchmarks/data/litqa2") -> list[dict]:  # type: ignore[return]
    """Load LitQA2 benchmark. Stub — implement in Phase 0."""
    raise NotImplementedError("Implement LitQA2 loader in Phase 0")


def load_ragtruth(cache_dir: str = "benchmarks/data/ragtruth") -> list[dict]:  # type: ignore[return]
    """Load RAGTruth benchmark. Stub — implement in Phase 0."""
    raise NotImplementedError("Implement RAGTruth loader in Phase 0")


def load_halubench(cache_dir: str = "benchmarks/data/halubench") -> list[dict]:  # type: ignore[return]
    """Load HaluBench benchmark. Stub — implement in Phase 0."""
    raise NotImplementedError("Implement HaluBench loader in Phase 0")
