"""Span-level evaluation metrics.

All metrics operate on (predicted, reference) pairs where references carry
exact character-span ground truth. Implement metrics here before tuning any
pipeline hyperparameter — eval before optimization.
"""
from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class CitationMetrics:
    """Span-level citation quality."""

    precision: float     # of cited spans, fraction that actually support the claim
    recall: float        # of supporting spans, fraction that were cited
    f1: float
    span_tightness: float  # 1.0 = exact, >1 = over-cited span


@dataclass(frozen=True)
class AbstentionMetrics:
    """Calibration of the abstention layer."""

    precision: float  # of refusals, fraction that were truly unsupported
    recall: float     # of unsupported claims, fraction that were refused
    f1: float


@dataclass(frozen=True)
class EvalResult:
    citation: CitationMetrics
    abstention: AbstentionMetrics
    localization_accuracy: float  # how closely cited spans match ground-truth spans


def citation_precision_recall(
    predicted_sentence_ids: list[list[str]],
    reference_sentence_ids: list[list[str]],
) -> CitationMetrics:
    """Compute citation P/R/F1 over a set of (predicted, reference) pairs.

    Both arguments are lists-of-lists: one inner list per generated sentence.
    This is a stub — implement in Phase 2.
    """
    raise NotImplementedError("Implement in Phase 2 (eval harness)")


def abstention_f1(
    refused: list[bool],
    truly_unsupported: list[bool],
) -> AbstentionMetrics:
    """Compute abstention P/R/F1.  Stub — implement in Phase 2."""
    raise NotImplementedError("Implement in Phase 2 (eval harness)")


def span_tightness(
    predicted_char_spans: list[tuple[int, int]],
    reference_char_spans: list[tuple[int, int]],
) -> float:
    """Ratio of predicted span length to reference span length.

    1.0 = perfect, >1 = over-cited.  Stub — implement in Phase 2.
    """
    raise NotImplementedError("Implement in Phase 2 (eval harness)")
