"""Built-in benchmarks for verifiable-rag eval harness.

Tier 1 ships with one benchmark:
  - HarryPotterMicroBench: 15 hand-curated questions on the cached HP book 1
    PDF in tests/parsers/fixtures/sample.pdf.

Tier 2 will add LitQA2, RAGTruth, HaluBench (currently stubs).
"""

from __future__ import annotations

from typing import Any

from verifiable_rag.eval.datasets.harry_potter import HarryPotterMicroBench


def load_litqa2(cache_dir: str = "benchmarks/data/litqa2") -> list[dict[str, Any]]:
    """Load LitQA2 benchmark. Stub — implement in Tier 2."""
    raise NotImplementedError("Implement LitQA2 loader in Tier 2")


def load_ragtruth(cache_dir: str = "benchmarks/data/ragtruth") -> list[dict[str, Any]]:
    """Load RAGTruth benchmark. Stub — implement in Tier 2."""
    raise NotImplementedError("Implement RAGTruth loader in Tier 2")


def load_halubench(cache_dir: str = "benchmarks/data/halubench") -> list[dict[str, Any]]:
    """Load HaluBench benchmark. Stub — implement in Tier 2."""
    raise NotImplementedError("Implement HaluBench loader in Tier 2")


__all__ = ["HarryPotterMicroBench", "load_litqa2", "load_ragtruth", "load_halubench"]
