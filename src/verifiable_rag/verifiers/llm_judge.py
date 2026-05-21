"""LLMJudgeVerifier — ask a chat LLM whether each claim is supported.

For each ``(premise, hypothesis)`` pair we send a JSON-output prompt and
read back ``{"supported": bool, "confidence": float in [0, 1]}``.
``score_pairs`` returns ``confidence * (supported ? 1 : 0) + (1-confidence)*(supported ? 0.5 : 0.5/2)``
— the boolean is the dominant signal; confidence smooths near-call edges
so calibration metrics on the raw score remain meaningful.

This verifier exists for two reasons:

1. **Strong baseline.** LLM-judge with a frontier model is the de-facto
   ceiling on RAGTruth (Sonnet-level judges report ~0.85 response F1).
   We need the comparison number for the blog post.
2. **Cheap alternative.** Haiku-class judges are 10-50x cheaper than
   Sonnet and only a few points worse. Quantifying that tradeoff is
   exactly what RAGTruth lets us do.

Only implements :class:`NLIScorer` for now; pairs with the RAGTruth
runner. The full :class:`Verifier`-protocol wiring (CitedSentence →
VerificationResult) arrives when we plumb this into the Pipeline.
"""

from __future__ import annotations

import json
import logging
from concurrent.futures import ThreadPoolExecutor
from typing import Any

logger = logging.getLogger(__name__)


_DEFAULT_SYSTEM = (
    "You are a strict fact-checker. Given a passage and a claim, decide "
    "whether the passage *directly entails* the claim. The claim must be "
    "supported by what the passage actually says, not by world knowledge "
    "or plausible inference. Reply with JSON: "
    '{"supported": true|false, "confidence": <0.0-1.0>}. '
    "Set confidence based on how clearly the passage supports (or fails "
    "to support) the claim — never below 0.5."
)


class LLMJudgeVerifier:
    """LLM-as-judge faithfulness scorer.

    Parameters
    ----------
    model:
        LiteLLM model identifier. Default ``"claude-haiku-4-5-20251001"``
        (cheap, fast, capable enough for most claims).
    temperature:
        Sampling temperature. Default ``0.0`` for deterministic judgments
        — calibration depends on reproducibility.
    max_tokens:
        Cap on the response. JSON output is tiny (~30 tokens) so 64 is
        plenty; the default leaves headroom.
    max_workers:
        ThreadPoolExecutor size for concurrent ``litellm.completion``
        calls. Default 8 — beyond that, provider rate-limits dominate.
    num_retries:
        LiteLLM's built-in retry count for transient errors.
    system_prompt:
        Override the default fact-checker instruction.
    """

    def __init__(
        self,
        model: str = "claude-haiku-4-5-20251001",
        temperature: float = 0.0,
        max_tokens: int = 128,
        max_workers: int = 8,
        num_retries: int = 2,
        system_prompt: str = _DEFAULT_SYSTEM,
    ) -> None:
        self._model = model
        self._temperature = temperature
        self._max_tokens = max_tokens
        self._max_workers = max_workers
        self._num_retries = num_retries
        self._system_prompt = system_prompt

    # ------------------------------------------------------------------ #
    # NLIScorer Protocol
    # ------------------------------------------------------------------ #

    def score_pairs(self, pairs: list[tuple[str, str]]) -> list[float]:
        """Score a batch of ``(premise, hypothesis)`` pairs.

        Empty premise or hypothesis scores 0.0. Each surviving pair is
        an independent LLM call, dispatched via a ThreadPoolExecutor so
        a batch of 32 doesn't take 32× the per-call latency.
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

        if self._max_workers > 1 and len(keep_pairs) > 1:
            with ThreadPoolExecutor(max_workers=self._max_workers) as pool:
                raw = list(pool.map(self._score_one, keep_pairs))
        else:
            raw = [self._score_one(pair) for pair in keep_pairs]

        for idx, s in zip(keep_idx, raw, strict=True):
            scores[idx] = float(s)
        return scores

    # ------------------------------------------------------------------ #
    # Internals
    # ------------------------------------------------------------------ #

    def _score_one(self, pair: tuple[str, str]) -> float:
        premise, hypothesis = pair
        try:
            raw_text = self._call_llm(premise, hypothesis)
        except Exception as exc:  # noqa: BLE001 — one bad call shouldn't tank the batch
            logger.warning("LLMJudge call failed: %s: %s", type(exc).__name__, exc)
            return 0.0
        return _parse_judgment(raw_text)

    def _call_llm(self, premise: str, hypothesis: str) -> str:
        """Send a (premise, hypothesis) pair to the LLM and return its raw output.

        Uses Anthropic prompt-cache breakpoints on the system prompt and
        the premise — within ~4 calls sharing the same premise (the
        sentences of one RAGTruth response), Anthropic returns cached
        reads at ~10% of the write cost. The ``cache_control`` field is
        silently ignored by non-Anthropic providers via LiteLLM, so the
        same code works for OpenAI / Gemini etc.

        Caveat: Anthropic's minimum cacheable block size is ~1024
        tokens. Below that the cache_control hint is silently ignored
        (no penalty, no benefit). Helps most on long-context tasks
        (Summary); minimal on short ones (QA).
        """
        try:
            import litellm
        except ImportError as exc:
            raise ImportError(
                "litellm is required for LLMJudgeVerifier. "
                "Install with: pip install 'verifiable-rag[litellm]'"
            ) from exc
        messages = [
            {
                "role": "system",
                "content": [
                    {
                        "type": "text",
                        "text": self._system_prompt,
                        "cache_control": {"type": "ephemeral"},
                    }
                ],
            },
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": f"PASSAGE:\n{premise}",
                        "cache_control": {"type": "ephemeral"},
                    },
                    {
                        "type": "text",
                        "text": f"CLAIM:\n{hypothesis}\n\nRespond with JSON only.",
                    },
                ],
            },
        ]
        response = litellm.completion(
            model=self._model,
            messages=messages,
            temperature=self._temperature,
            max_tokens=self._max_tokens,
            num_retries=self._num_retries,
        )
        return str(response.choices[0].message.content or "").strip()


def _parse_judgment(raw: str) -> float:
    """Map a JSON judgment string → entailment probability in ``[0, 1]``.

    The boolean ``supported`` is the dominant signal; ``confidence``
    shapes the magnitude inside each half-interval so high-confidence
    "supported" → ~1.0 and high-confidence "not supported" → ~0.0.
    """
    text = raw.strip()
    # Strip code fences if present
    if text.startswith("```"):
        # Drop the opening fence + optional "json" marker
        text = text.split("\n", 1)[-1] if "\n" in text else text[3:]
        if text.endswith("```"):
            text = text[:-3]
        text = text.strip()
    # Find first { ... } block tolerantly
    start = text.find("{")
    end = text.rfind("}")
    if start == -1 or end == -1 or end <= start:
        return 0.0
    try:
        obj = json.loads(text[start : end + 1])
    except json.JSONDecodeError:
        return 0.0
    if not isinstance(obj, dict):
        return 0.0
    supported = bool(obj.get("supported", False))
    conf = obj.get("confidence", 0.5)
    try:
        conf_f = float(conf)
    except (TypeError, ValueError):
        conf_f = 0.5
    # Clamp into [0.5, 1.0] so the boolean dominates.
    conf_f = max(0.5, min(1.0, conf_f))
    if supported:
        # supported → [0.5, 1.0]: high conf → ~1.0, low conf → 0.5
        return conf_f
    # not supported → [0.0, 0.5]: high conf → ~0.0, low conf → 0.5
    return 1.0 - conf_f


__all__ = ["LLMJudgeVerifier"]
