"""Eval runner — orchestrates benchmark execution and report generation.

Implement in Phase 2. The structure is defined here so CI can reference
the entry point.
"""
from __future__ import annotations

from pathlib import Path
from typing import Any

from verifiable_rag.pipeline import Pipeline


def run_eval(
    pipeline: Pipeline,
    dataset: str,
    output_path: Path,
    ci_subset: bool = False,
    max_examples: int | None = None,
) -> dict[str, Any]:
    """Run *pipeline* against *dataset* and write a markdown report to *output_path*.

    Args:
        pipeline:     Configured Pipeline to evaluate.
        dataset:      One of "litqa2", "ragtruth", "faithbench", "haluBench".
        output_path:  Where to write the markdown report.
        ci_subset:    If True, use a small fixed subset for fast CI runs.
        max_examples: Hard cap on examples (overrides ci_subset if smaller).

    Returns:
        Dict of metric names to float values.

    Stub — implement in Phase 2.
    """
    raise NotImplementedError("Implement in Phase 2 (eval harness)")
