"""DualNLIVerifier — Pipeline-compatible dual-NLI ensemble.

Combines two :class:`NLIScorer` instances (typically HHEM + MiniCheck)
into a single :class:`Verifier` that drops into ``Pipeline(verifier=...)``.

For each CitedSentence:

1. Build the **premise** by concatenating the texts of the cited
   sentence IDs (and only those IDs — not the full chunk).
2. Score the ``(premise, claim)`` pair via the underlying
   :class:`EnsembleScorer` (each scorer in sequence, then aggregate).
3. Compare against ``threshold`` to set the boolean ``is_supported``
   flag on the :class:`VerificationResult`.

Why this is the library's recommended default
---------------------------------------------
Per [benchmarks/PUBLISHED_ragtruth.md](../../../benchmarks/PUBLISHED_ragtruth.md),
on RAGTruth the dual NLI ensemble (HHEM + MiniCheck, min aggregation)
matches a Sonnet 4.6 LLM-judge on AUROC (0.844 vs 0.846) and calibrated
F1 (0.706 vs 0.707) at >100× lower per-call cost.

Default threshold (0.0562) is the value fit on RAGTruth-train with min
aggregation across HHEM-2.1-open + MiniCheck-Flan-T5-Large. Users with
domain-specific calibration data should fit their own threshold via
``scripts/compute_calibrated_metrics.py``.
"""

from __future__ import annotations

from verifiable_rag.models.answer import CitedSentence, VerificationResult
from verifiable_rag.models.document import Document
from verifiable_rag.verifiers.ensemble import EnsembleScorer


class DualNLIVerifier:
    """Two-scorer NLI ensemble implementing the :class:`Verifier` Protocol.

    Parameters
    ----------
    scorer_a, scorer_b:
        Any objects implementing :class:`NLIScorer`. Typically
        ``HHEMVerifier()`` and ``MiniCheckVerifier()``.
    aggregation:
        How to collapse the two scorer outputs per pair. ``"min"``
        (default) flags an example if *either* scorer is below
        threshold — matches HALT-RAG and our RAGTruth-published config.
        ``"mean"`` and ``"max"`` also supported for ablations.
    threshold:
        Cutoff for ``is_supported`` on each VerificationResult. Default
        ``0.0562`` is fit on RAGTruth-train with ``min`` aggregation
        across HHEM + MiniCheck. **Re-fit for your own data via
        scripts/compute_calibrated_metrics.py if your domain differs.**
    """

    def __init__(
        self,
        scorer_a,  # type: ignore[no-untyped-def] — NLIScorer (Protocol from sibling module)
        scorer_b,
        aggregation: str = "min",
        threshold: float = 0.0562,
    ) -> None:
        if not (0.0 <= threshold <= 1.0):
            raise ValueError(f"threshold must be in [0, 1], got {threshold}")
        self._ensemble = EnsembleScorer(
            [scorer_a, scorer_b], aggregation=aggregation
        )
        self._threshold = threshold
        self._aggregation = aggregation

    # ------------------------------------------------------------------ #
    # Verifier Protocol
    # ------------------------------------------------------------------ #

    def verify(
        self,
        sentences: list[CitedSentence],
        documents: dict[str, Document],
    ) -> list[VerificationResult]:
        """Return one VerificationResult per CitedSentence, in input order."""
        if not sentences:
            return []

        scored_pairs: list[tuple[str, str]] = []
        pair_to_sentence: list[int] = []

        for i, cs in enumerate(sentences):
            premise = _build_premise(cs.supporting_sentence_ids, documents)
            if not premise.strip() or not cs.text.strip():
                continue
            scored_pairs.append((premise, cs.text))
            pair_to_sentence.append(i)

        if scored_pairs:
            raw_scores = self._ensemble.score_pairs(scored_pairs)
        else:
            raw_scores = []

        scores_by_sentence_idx: dict[int, float] = {
            idx: float(s)
            for idx, s in zip(pair_to_sentence, raw_scores, strict=True)
        }

        results: list[VerificationResult] = []
        for i, cs in enumerate(sentences):
            score = scores_by_sentence_idx.get(i, 0.0)
            results.append(
                VerificationResult(
                    cited_sentence_index=i,
                    claim_text=cs.text,
                    is_supported=score >= self._threshold,
                    nli_score=score,
                )
            )
        return results

    # ------------------------------------------------------------------ #
    # NLIScorer Protocol — pass-through to the ensemble
    # ------------------------------------------------------------------ #

    def score_pairs(self, pairs: list[tuple[str, str]]) -> list[float]:
        """Raw (premise, hypothesis) scoring — used by RAGTruth runner."""
        return self._ensemble.score_pairs(pairs)


def _build_premise(
    supporting_sentence_ids: tuple[str, ...],
    documents: dict[str, Document],
) -> str:
    """Concatenate the text of every cited sentence we can find.

    Mirrors :func:`HHEMVerifier._build_premise` — looks across all
    provided documents (sentence ids carry their doc_id by convention
    but downstream code shouldn't have to peel that apart).
    """
    texts: list[str] = []
    for sid in supporting_sentence_ids:
        for doc in documents.values():
            try:
                sent = doc.sentence_by_id(sid)
                texts.append(sent.text)
                break
            except KeyError:
                continue
    return " ".join(texts)


__all__ = ["DualNLIVerifier"]
