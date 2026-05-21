"""MiniCheckVerifier — Flan-T5-based NLI verifier from Liyan Tang et al. 2024.

Loads ``lytang/MiniCheck-Flan-T5-Large`` directly via transformers (no
``minicheck`` package dependency). For each ``(premise, hypothesis)`` pair:

1. Format as the model's expected input: ``"premise: {p} hypothesis: {h}"``.
2. Generate one token deterministically.
3. Take the softmax over the model's "1" (entailed) vs "0" (not entailed)
   token logits → entailment probability in ``[0, 1]``.

Why this and not HHEM? Different training distribution:

* HHEM: Vectara's summarization-style entailment data (~600M params).
* MiniCheck: synthetic claim decompositions, multi-domain (~770M for the
  Flan-T5-Large variant).

The HALT-RAG paper (Sept 2025) showed their false-positive sets overlap
less than two-of-the-same-model would — so an ensemble (future
``DualNLIVerifier``) reduces FN at fixed FP on RAGTruth.

Only implements :class:`NLIScorer` for now; full
:class:`Verifier`-protocol wiring (CitedSentence → VerificationResult)
arrives when we plumb this into the Pipeline (Phase 4 Week 11).
"""

from __future__ import annotations

from typing import Any


class MiniCheckVerifier:
    """NLI verifier backed by MiniCheck-Flan-T5-Large.

    Parameters
    ----------
    model_name:
        HuggingFace id. Default ``"lytang/MiniCheck-Flan-T5-Large"``.
    device:
        ``"cpu"``, ``"cuda"``, ``"mps"``, or ``None`` to autodetect.
    max_input_length:
        Token cap for the (premise, hypothesis) concatenation. Long
        premises get truncated from the right (preserving the claim
        text); 2048 covers >95% of RAGTruth contexts.
    """

    def __init__(
        self,
        model_name: str = "lytang/MiniCheck-Flan-T5-Large",
        device: str | None = None,
        max_input_length: int = 2048,
    ) -> None:
        self._model_name = model_name
        self._device = device
        self._max_input_length = max_input_length
        self._tokenizer: Any = None
        self._model: Any = None
        self._yes_id: int | None = None
        self._no_id: int | None = None

    # ------------------------------------------------------------------ #
    # NLIScorer Protocol
    # ------------------------------------------------------------------ #

    def score_pairs(self, pairs: list[tuple[str, str]]) -> list[float]:
        """Score a batch of ``(premise, hypothesis)`` pairs.

        Empty premise OR empty hypothesis scores 0.0; the rest go
        through MiniCheck in one batched forward pass.
        """
        if not pairs:
            return []

        keep_idx: list[int] = []
        keep_pairs: list[tuple[str, str]] = []
        for i, (p, h) in enumerate(pairs):
            if p.strip() and h.strip():
                keep_idx.append(i)
                keep_pairs.append((p, h))

        scores = [0.0] * len(pairs)
        if not keep_pairs:
            return scores

        tokenizer, model = self._load()
        import torch

        texts = [f"premise: {p} hypothesis: {h}" for p, h in keep_pairs]
        inputs = tokenizer(
            texts,
            return_tensors="pt",
            padding=True,
            truncation=True,
            max_length=self._max_input_length,
        )
        if self._device is not None:
            inputs = {k: v.to(self._device) for k, v in inputs.items()}

        with torch.no_grad():
            outputs = model.generate(
                **inputs,
                max_new_tokens=1,
                output_scores=True,
                return_dict_in_generate=True,
                do_sample=False,
            )
        # outputs.scores is a tuple of length max_new_tokens; first
        # element has shape (batch, vocab).
        first_token_logits = outputs.scores[0]
        assert self._yes_id is not None and self._no_id is not None
        two_class = torch.stack(
            [first_token_logits[:, self._no_id], first_token_logits[:, self._yes_id]],
            dim=-1,
        )
        probs = torch.softmax(two_class, dim=-1)[:, 1]
        raw = probs.detach().cpu().tolist()

        for idx, s in zip(keep_idx, raw, strict=True):
            scores[idx] = float(s)
        return scores

    # ------------------------------------------------------------------ #
    # Internals
    # ------------------------------------------------------------------ #

    def _load(self) -> tuple[Any, Any]:
        if self._tokenizer is not None and self._model is not None:
            return self._tokenizer, self._model

        try:
            from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
        except ImportError as exc:
            raise ImportError(
                "transformers is required for MiniCheckVerifier. "
                "Install with: pip install 'verifiable-rag[minicheck]'"
            ) from exc

        self._tokenizer = AutoTokenizer.from_pretrained(self._model_name)
        kwargs: dict[str, Any] = {}
        if self._device is not None:
            kwargs["device_map"] = self._device
        self._model = AutoModelForSeq2SeqLM.from_pretrained(self._model_name, **kwargs)
        self._model.eval()

        # Cache the *first* token IDs of the "1" / "0" label encodings.
        # Flan-T5's SentencePiece tokenizer is asymmetric here: "1"
        # encodes to a single token, but "0" gets a SentencePiece-marker
        # prefix (so "0" → [3, 632]). The model was trained on these full
        # encodings and emits tokens autoregressively, so the FIRST token
        # of each encoding is what the model produces at the first
        # decoder step — that's the position-0 discriminator we read off.
        yes_ids = self._tokenizer("1", add_special_tokens=False).input_ids
        no_ids = self._tokenizer("0", add_special_tokens=False).input_ids
        if not yes_ids or not no_ids:
            raise RuntimeError(
                f"Empty tokenizer encoding for '1'/'0' (got {yes_ids!r}/"
                f"{no_ids!r}) — incompatible tokenizer."
            )
        self._yes_id = yes_ids[0]
        self._no_id = no_ids[0]
        return self._tokenizer, self._model


__all__ = ["MiniCheckVerifier"]
