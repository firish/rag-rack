"""Built-in benchmarks for verifiable-rag eval harness.

Currently shipping:
  - HarryPotterMicroBench: 29 hand-curated questions on the cached HP book 1
    PDF (tests/parsers/fixtures/sample.pdf).
  - LitQA2Bench: 199 multi-choice scientific-paper questions from the
    LAB-Bench dataset on HuggingFace.

Planned: RAGTruth (faithfulness calibration), HaluBench (hallucination).
"""

from __future__ import annotations

from typing import Any

from verifiable_rag.eval.datasets.alce import ALCEBench, supported_subbenches
from verifiable_rag.eval.datasets.harry_potter import HarryPotterMicroBench
from verifiable_rag.eval.datasets.litqa2 import LitQA2Bench, load_litqa2_meta


def load_ragtruth(cache_dir: str = "benchmarks/data/ragtruth") -> list[dict[str, Any]]:
    """Load RAGTruth benchmark. Stub — implement when needed for verifier calibration."""
    raise NotImplementedError("RAGTruth loader not yet implemented")


def load_halubench(cache_dir: str = "benchmarks/data/halubench") -> list[dict[str, Any]]:
    """Load HaluBench benchmark. Stub — implement when needed."""
    raise NotImplementedError("HaluBench loader not yet implemented")


__all__ = [
    "ALCEBench",
    "HarryPotterMicroBench",
    "LitQA2Bench",
    "load_halubench",
    "load_litqa2_meta",
    "load_ragtruth",
    "supported_subbenches",
]
