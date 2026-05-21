"""Built-in benchmarks for verifiable-rag eval harness.

Currently shipping:
  - HarryPotterMicroBench: 29 hand-curated questions on the cached HP book 1
    PDF (tests/parsers/fixtures/sample.pdf).
  - LitQA2Bench: 199 multi-choice scientific-paper questions from the
    LAB-Bench dataset on HuggingFace.
  - ALCEBench: Princeton's citation-quality benchmark (ASQA/QAMPARI/ELI5).
  - RAGTruthBench: word-span hallucination annotations (verifier benchmark).

Planned: HaluBench (binary hallucination), FaithBench (gated on HF).
"""

from __future__ import annotations

from typing import Any

from verifiable_rag.eval.datasets.alce import ALCEBench, supported_subbenches
from verifiable_rag.eval.datasets.harry_potter import HarryPotterMicroBench
from verifiable_rag.eval.datasets.litqa2 import LitQA2Bench, load_litqa2_meta
from verifiable_rag.eval.datasets.ragtruth import (
    HallucinationSpan,
    RAGTruthBench,
    RAGTruthExample,
)


def load_halubench(cache_dir: str = "benchmarks/data/halubench") -> list[dict[str, Any]]:
    """Load HaluBench benchmark. Stub — implement when needed."""
    raise NotImplementedError("HaluBench loader not yet implemented")


__all__ = [
    "ALCEBench",
    "HallucinationSpan",
    "HarryPotterMicroBench",
    "LitQA2Bench",
    "RAGTruthBench",
    "RAGTruthExample",
    "load_halubench",
    "load_litqa2_meta",
    "supported_subbenches",
]
