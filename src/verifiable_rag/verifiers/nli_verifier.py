"""NLIVerifier — adapt any :class:`NLIScorer` into a :class:`Verifier`.

The library has two related Protocols:

* :class:`NLIScorer` — raw ``(premise, hypothesis) → float`` scoring.
* :class:`Verifier` — the Pipeline-facing interface that takes
  :class:`CitedSentence` + :class:`Document` and returns a
  :class:`VerificationResult` per sentence.

Several scorers (:class:`MiniCheckVerifier`, :class:`LLMJudgeVerifier`,
:class:`ModalHHEMScorer`, …) implement only the NLI interface.
:class:`NLIVerifier` is the bridge — it builds premises from cited sentence
IDs, calls ``scorer.score_pairs``, and wraps the results as
:class:`VerificationResult` objects.

Mirrors the same internal logic that :class:`HHEMVerifier` and
:class:`DualNLIVerifier` use directly. Use it when you want any single
scorer (especially :class:`LLMJudgeVerifier`) as the Pipeline verifier.

Example
-------
::

    from verifiable_rag import Pipeline
    from verifiable_rag.verifiers import LLMJudgeVerifier, NLIVerifier

    judge = LLMJudgeVerifier(model="anthropic/claude-sonnet-4-6")
    pipeline = Pipeline(
        ...,
        verifier=NLIVerifier(judge, threshold=0.5),
    )

Or use the :func:`llm_judge_verified <verifiable_rag.presets.llm_judge_verified>`
preset which wires this for you.
"""

from __future__ import annotations

from verifiable_rag.models.answer import CitedSentence, VerificationResult
from verifiable_rag.models.document import Document


class NLIVerifier:
    """Wrap any :class:`NLIScorer` to implement the :class:`Verifier` Protocol.

    Parameters
    ----------
    scorer:
        Any object implementing ``score_pairs(pairs) -> list[float]``.
        Typically :class:`LLMJudgeVerifier`, :class:`MiniCheckVerifier`,
        or :class:`ModalHHEMScorer`.
    threshold:
        Cutoff for ``is_supported`` on each :class:`VerificationResult`.
        Score ``>= threshold`` → supported. Default ``0.5`` is a sensible
        neutral cutoff; for production use, calibrate on your domain via
        ``scripts/compute_calibrated_metrics.py``.
    """

    def __init__(
        self,
        scorer,  # type: ignore[no-untyped-def] — any NLIScorer
        threshold: float = 0.5,
    ) -> None:
        if not (0.0 <= threshold <= 1.0):
            raise ValueError(f"threshold must be in [0, 1], got {threshold}")
        self._scorer = scorer
        self._threshold = threshold

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

        scores_by_idx: dict[int, float] = {}
        if scored_pairs:
            raw = self._scorer.score_pairs(scored_pairs)
            scores_by_idx = {
                idx: float(s)
                for idx, s in zip(pair_to_sentence, raw, strict=True)
            }

        results: list[VerificationResult] = []
        for i, cs in enumerate(sentences):
            score = scores_by_idx.get(i, 0.0)
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
    # NLIScorer Protocol — pass-through to the underlying scorer
    # ------------------------------------------------------------------ #

    def score_pairs(self, pairs: list[tuple[str, str]]) -> list[float]:
        """Raw scoring pass-through — same as the underlying scorer."""
        return self._scorer.score_pairs(pairs)


def _build_premise(
    supporting_sentence_ids: tuple[str, ...],
    documents: dict[str, Document],
) -> str:
    """Concatenate the text of every cited sentence we can find.

    Same logic as ``HHEMVerifier._build_premise`` and
    ``DualNLIVerifier._build_premise`` — looks across all provided
    documents (sentence ids carry their doc_id by convention).
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


__all__ = ["NLIVerifier"]
