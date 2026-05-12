"""HHEMVerifier: NLI-based faithfulness verifier using Vectara's HHEM-2.1-open.

For each :class:`CitedSentence`:

1. Build the **premise** by concatenating the texts of the cited sentence
   IDs (and ONLY those IDs — not the full surrounding chunk). This is a
   deliberate choice: it catches the failure mode where the LLM cites
   sentence X but the actual support is sentence Y in the same chunk.
2. Feed ``(premise, claim_text)`` through HHEM-2.1-open, which returns a
   probability in ``[0, 1]`` (0 = unsupported / hallucinated, 1 = entailed).
3. Wrap the result in a :class:`VerificationResult`.

Pipeline downstream uses these scores (via ``faithfulness_score``
aggregation + strictness threshold) to flag or refuse unsupported claims.

Notes
-----
- This is the **sentence-level** MVP. Atomic claim decomposition (a
  follow-up LLM call to split synthesized sentences into atomic factoids)
  is planned but not implemented. Sentence-level captures the
  architectural verification step; atomic adds per-claim granularity.
- ``trust_remote_code=True`` is required by HHEM-2.1-open (custom model
  class). Standard practice for this model — documented for awareness.
"""

from __future__ import annotations

from typing import Any

from verifiable_rag.models.answer import CitedSentence, VerificationResult
from verifiable_rag.models.document import Document


class HHEMVerifier:
    """Sentence-level NLI verifier backed by HHEM-2.1-open.

    Parameters
    ----------
    model_name:
        HuggingFace model id. Default
        ``"vectara/hallucination_evaluation_model"`` (HHEM-2.1-open, ~600M).
    threshold:
        Cutoff for the boolean ``is_supported`` flag on each
        VerificationResult. Pipeline strictness controls a separate
        refusal threshold; this one is just per-claim. Default 0.5.
    device:
        ``"cpu"``, ``"cuda"``, ``"mps"``, or ``None`` to autodetect.
    """

    def __init__(
        self,
        model_name: str = "vectara/hallucination_evaluation_model",
        threshold: float = 0.5,
        device: str | None = None,
    ) -> None:
        if not (0.0 <= threshold <= 1.0):
            raise ValueError(f"threshold must be in [0, 1], got {threshold}")
        self._model_name = model_name
        self._threshold = threshold
        self._device = device
        self._model: Any = None

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

        # Build (premise, hypothesis) pairs, tracking which sentence-indices
        # actually have a non-empty premise. Indices with no premise score 0.
        scored_pairs: list[tuple[str, str]] = []
        pair_to_sentence: list[int] = []

        for i, cs in enumerate(sentences):
            premise = self._build_premise(cs.supporting_sentence_ids, documents)
            if not premise.strip() or not cs.text.strip():
                continue
            scored_pairs.append((premise, cs.text))
            pair_to_sentence.append(i)

        # Score everything in one batch call to the model.
        if scored_pairs:
            model = self._load()
            raw_scores = model.predict(scored_pairs)
        else:
            raw_scores = []

        scores_by_sentence_idx: dict[int, float] = {
            sentence_idx: float(score)
            for sentence_idx, score in zip(pair_to_sentence, raw_scores, strict=True)
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
    # Internals
    # ------------------------------------------------------------------ #

    @staticmethod
    def _build_premise(
        supporting_sentence_ids: tuple[str, ...],
        documents: dict[str, Document],
    ) -> str:
        """Concatenate the text of every cited sentence we can find.

        We look across ALL provided documents (not just the one matching
        the sentence id's doc prefix) because sentence ids carry their
        doc_id by convention but downstream code shouldn't have to peel
        that apart.
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

    def _load(self) -> Any:
        if self._model is not None:
            return self._model

        try:
            from transformers import AutoModelForSequenceClassification
        except ImportError as exc:
            raise ImportError(
                "transformers is required for HHEMVerifier. "
                "Install with: pip install 'verifiable-rag[hhem]'"
            ) from exc

        kwargs: dict[str, Any] = {"trust_remote_code": True}
        if self._device is not None:
            kwargs["device_map"] = self._device

        self._model = AutoModelForSequenceClassification.from_pretrained(
            self._model_name,
            **kwargs,
        )
        return self._model
