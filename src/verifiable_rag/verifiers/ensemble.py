"""EnsembleScorer — combine multiple NLIScorers into one.

For each ``(premise, hypothesis)`` pair, every underlying scorer
produces a probability. The ensemble aggregates them per pair via
``min`` / ``mean`` / ``max``:

* ``min``  → conservative (HALT-RAG convention): if *any* scorer says
            unsupported, the ensemble says unsupported.
* ``mean`` → average — smoother across scorer-specific noise.
* ``max``  → lenient: if any scorer says supported, the ensemble does.

Itself implements the :class:`NLIScorer` Protocol, so it composes:
``EnsembleScorer([s1, s2, s3])`` is itself a valid scorer that can be
wrapped by :class:`DualNLIVerifier` or fed into the RAGTruth runner.

Speed note: each pair is scored once *per underlying scorer*. The
ensemble of two GPU verifiers therefore does two GPU forward passes
per batch. Cost adds linearly.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from verifiable_rag.verifiers import NLIScorer

_AGGREGATIONS = frozenset({"min", "mean", "max"})


class EnsembleScorer:
    """Combine multiple :class:`NLIScorer` instances into one.

    Parameters
    ----------
    scorers:
        Two or more objects satisfying :class:`NLIScorer`.
    aggregation:
        How to collapse per-pair scores across scorers. ``"min"`` (default)
        matches HALT-RAG and our RAGTruth-published configuration.
    """

    def __init__(
        self,
        scorers: list["NLIScorer"],
        aggregation: str = "min",
    ) -> None:
        if len(scorers) < 2:
            raise ValueError(
                f"EnsembleScorer requires ≥2 scorers, got {len(scorers)}"
            )
        if aggregation not in _AGGREGATIONS:
            raise ValueError(
                f"aggregation must be one of {sorted(_AGGREGATIONS)}, got "
                f"{aggregation!r}"
            )
        self._scorers = list(scorers)
        self._aggregation = aggregation

    def score_pairs(self, pairs: list[tuple[str, str]]) -> list[float]:
        if not pairs:
            return []
        # One call per scorer — each handles its own batching internally.
        scores_per_scorer = [s.score_pairs(pairs) for s in self._scorers]
        # Sanity: all must return the same length as `pairs`.
        for i, scores in enumerate(scores_per_scorer):
            if len(scores) != len(pairs):
                raise RuntimeError(
                    f"scorer[{i}] returned {len(scores)} scores for "
                    f"{len(pairs)} pairs — length mismatch"
                )
        out: list[float] = []
        for per_pair in zip(*scores_per_scorer, strict=True):
            if self._aggregation == "min":
                out.append(float(min(per_pair)))
            elif self._aggregation == "mean":
                out.append(float(sum(per_pair) / len(per_pair)))
            else:  # "max"
                out.append(float(max(per_pair)))
        return out


__all__ = ["EnsembleScorer"]
