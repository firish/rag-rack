"""Modal-hosted GPU verifiers.

Two classes — :class:`HHEMRemote` (Vectara HHEM-2.1-open) and
:class:`MiniCheckRemote` (lytang/MiniCheck-Flan-T5-Large) — exposing the
same ``score_pairs`` method as the local NLIScorer Protocol so they
drop into ``run_ragtruth`` unchanged.

Deploy:
    modal deploy infra/modal_verifiers.py

After deploy the local wrappers in
``src.verifiable_rag.verifiers.modal_remote`` look these up by app name
and call ``.remote()`` on each batch.

Cost note (T4 @ $0.59/hr): 600 examples × ~4 sentences ≈ 2400 NLI calls;
on T4 that's roughly 2–5 min of GPU time per verifier (~$0.05 each).
``scaledown_window=600`` keeps the warm container around for 10 minutes
so back-to-back runs share the warmed model + cold start.
"""

from __future__ import annotations

import modal

GPU = "T4"  # cheapest GPU that fits both models comfortably (~16GB VRAM)
# Short scaledown: free the GPU slot fast after a run finishes so another
# verifier can claim it. Concurrency caps on free/starter tiers cap us at
# 1 GPU container; a long warm hold blocks parallel runs.
SCALEDOWN_SECONDS = 30

image = (
    modal.Image.debian_slim(python_version="3.11")
    .pip_install(
        "torch>=2.2",
        "transformers>=4.40,<4.50",
        "huggingface_hub",
        "sentencepiece",  # required by MiniCheck's Flan-T5 tokenizer
        "accelerate",  # transformers loaders benefit from this on GPU
    )
)

app = modal.App("verifiable-rag-verifiers", image=image)


# --------------------------------------------------------------------------- #
# HHEM-2.1-open (Vectara)
# --------------------------------------------------------------------------- #


@app.cls(gpu=GPU, scaledown_window=SCALEDOWN_SECONDS, timeout=900)
class HHEMRemote:
    @modal.enter()
    def load(self) -> None:
        from transformers import AutoModelForSequenceClassification

        self.model = AutoModelForSequenceClassification.from_pretrained(
            "vectara/hallucination_evaluation_model",
            trust_remote_code=True,
        )
        self.model = self.model.to("cuda")
        self.model.eval()

    @modal.method()
    def score_pairs(self, pairs: list[tuple[str, str]]) -> list[float]:
        if not pairs:
            return []
        # HHEM's custom predict() handles tokenization + batching.
        raw = self.model.predict(pairs)
        return [float(s) for s in raw]


# --------------------------------------------------------------------------- #
# MiniCheck-Flan-T5-Large (Tang et al. 2024)
# --------------------------------------------------------------------------- #


@app.cls(gpu=GPU, scaledown_window=SCALEDOWN_SECONDS, timeout=900)
class MiniCheckRemote:
    @modal.enter()
    def load(self) -> None:
        import torch
        from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

        self.tokenizer = AutoTokenizer.from_pretrained("lytang/MiniCheck-Flan-T5-Large")
        self.model = AutoModelForSeq2SeqLM.from_pretrained(
            "lytang/MiniCheck-Flan-T5-Large",
        )
        self.model = self.model.to("cuda")
        self.model.eval()

        # Flan-T5 SentencePiece asymmetry: "1" encodes to a single token
        # but "0" gets a leading SP-marker (e.g. [3, 632]). The model
        # emits tokens autoregressively from its training-label
        # encoding, so the FIRST token of each is the position-0
        # discriminator we read off the logits.
        yes_ids = self.tokenizer("1", add_special_tokens=False).input_ids
        no_ids = self.tokenizer("0", add_special_tokens=False).input_ids
        if not yes_ids or not no_ids:
            raise RuntimeError(
                f"Empty tokenizer encoding for '1'/'0': {yes_ids!r}/{no_ids!r}"
            )
        self.yes_id = yes_ids[0]
        self.no_id = no_ids[0]
        self._torch = torch  # cache module ref for tight loop

    @modal.method()
    def score_pairs(self, pairs: list[tuple[str, str]]) -> list[float]:
        if not pairs:
            return []
        torch = self._torch

        texts = [f"premise: {p} hypothesis: {h}" for p, h in pairs]
        inputs = self.tokenizer(
            texts,
            return_tensors="pt",
            padding=True,
            truncation=True,
            max_length=2048,
        ).to("cuda")
        with torch.no_grad():
            outputs = self.model.generate(
                **inputs,
                max_new_tokens=1,
                output_scores=True,
                return_dict_in_generate=True,
                do_sample=False,
            )
        first_token_logits = outputs.scores[0]
        two_class = torch.stack(
            [
                first_token_logits[:, self.no_id],
                first_token_logits[:, self.yes_id],
            ],
            dim=-1,
        )
        probs = torch.softmax(two_class, dim=-1)[:, 1]
        return probs.detach().cpu().tolist()


@app.local_entrypoint()
def smoke() -> None:
    """`modal run infra/modal_verifiers.py::smoke` — quick sanity check."""
    pairs = [
        ("Paris is the capital of France.", "Paris is in France."),
        ("Paris is the capital of France.", "The moon is made of cheese."),
    ]
    print("HHEM:", HHEMRemote().score_pairs.remote(pairs))
    print("MiniCheck:", MiniCheckRemote().score_pairs.remote(pairs))
