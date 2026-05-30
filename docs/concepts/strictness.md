# Strictness & refusal

How the library decides when to return a partial answer, a clean answer, or a refusal.

## The strictness slider

`Pipeline.strictness` is a four-step slider that maps to a faithfulness threshold:

| Strictness | Threshold | Behavior |
|---|---|---|
| `loose` | 0.0 | Never refuse. Verifier output is informational only. |
| `balanced` ⭐ | 0.5 | Refuse if faithfulness score < 0.5 after surgical correction. **Default.** |
| `strict` | 0.7 | Refuse if faithfulness score < 0.7. Only confident answers slip through. |
| `paranoid` | 0.9 | Refuse if faithfulness score < 0.9. High refusal rate; for high-trust use cases. |

You can pass the strictness either to a preset (`hybrid_strict()`) or directly to the Pipeline:

```python
from verifiable_rag import hybrid_balanced

pipeline = hybrid_balanced()
pipeline.strictness = "strict"
```

Or wire it from scratch:

```python
from verifiable_rag import Pipeline
pipeline = Pipeline(..., strictness="paranoid")
```

## What "faithfulness score" actually is

After verification runs, the Pipeline computes a single scalar `faithfulness_score ∈ [0, 1]` that summarizes how trustworthy the answer is. It's a blend of three signals:

```python
faithfulness_score = combine(
    retrieval_score,       # avg retrieval / rerank score across used chunks
    nli_score,             # avg NLI score across cited sentences
    generation_logprob,    # generator-side confidence (when available)
)
```

The exact combination is implementation-controlled; the components are also exposed on `answer.faithfulness_components` for users who want to look at them separately.

## Surgical correction vs. hard refusal

When the verifier flags sentences as unsupported, the Pipeline has two options:

1. **Surgical correction** (default in `balanced`+): drop just the flagged sentences from the answer, return the rest. The dropped texts land on `answer.unsupported_claims`.
2. **Hard refusal**: drop everything and return an empty answer with `answer.was_refused = True` and a `refusal_reason`.

The decision is based on the post-correction faithfulness score:

```
verify → flag unsupported sentences
       → surgical correction (drop flagged sentences)
       → recompute faithfulness
       → IF faithfulness < strictness_threshold:
              hard refusal
         ELSE:
              return surgically corrected answer
```

## What an answer looks like in each mode

Same query, same document, four strictness levels. The query is *"Did the authors prove a causal mechanism?"* — a hard question where the document only provides correlational evidence.

=== "loose"

    ```python
    answer = verifiable_rag.ask(query, docs=..., preset="local_minimal")
    # answer.text         = "The authors demonstrated a causal link between..."
    # answer.was_refused  = False
    # No verifier ran. The LLM's output passes through unmodified.
    ```

=== "balanced"

    ```python
    pipeline = hybrid_balanced()
    answer = pipeline.ask(query)
    # answer.text         = "The authors observed a correlation between..."
    # answer.was_refused  = False
    # answer.unsupported_claims = ["The authors demonstrated a causal link"]
    # Verifier flagged the overreaching sentence; surgical correction kept the rest.
    ```

=== "strict"

    ```python
    pipeline = hybrid_strict()
    answer = pipeline.ask(query)
    # answer.text         = ""
    # answer.was_refused  = True
    # answer.refusal_reason = "post-correction faithfulness 0.42 below strict threshold 0.7"
    # The corrected answer didn't clear the bar, so refused.
    ```

=== "paranoid"

    ```python
    pipeline = hybrid_paranoid()  # uses Sonnet 4.6 as the generator
    answer = pipeline.ask(query)
    # answer.text         = ""
    # answer.was_refused  = True
    # answer.refusal_reason = "post-correction faithfulness 0.78 below paranoid threshold 0.9"
    ```

## Why this matters

Most "chat with your documents" products use prompt-conditioned refusal: they tell the LLM "if you don't know, say you don't know." This fails for the same reason every prompt-conditioned safety measure fails — the model is sometimes confidently wrong about what it knows.

The library's strictness slider is **architectural**: the refusal decision is made *after* the verifier has actually checked the cites against the source. The model can't talk its way past a faithfulness threshold; the threshold is computed from objective NLI scores.

This is also why `strict` and `paranoid` modes require a verifier:

> A `strict`-mode answer that didn't actually run verification is a bug, not a feature.

If you wire `verifier=None` and set `strictness="strict"`, the Pipeline raises. The library refuses to claim it verified something it didn't.

## Programmatic detection

```python
answer = pipeline.ask(query)

if answer.was_refused:
    log.warning(f"refused: {answer.refusal_reason}")
    # Optionally: retry with a looser strictness, or surface to user
    return None

if answer.unsupported_claims:
    log.info(f"answer included corrections; dropped: {answer.unsupported_claims}")

return answer.text
```

For aggregate observability (refusal rate, average faithfulness, etc.), every answer has `answer.audit_trail()` — a JSON-serializable dict ready for emission to your metrics stack. See [Observability](../how-to/observability.md).

## Choosing the right strictness

| If your use case is... | Pick... |
|---|---|
| Internal chatbot, low-stakes Q&A | `loose` or `balanced` |
| User-facing product, citation matters | `balanced` (default) |
| Legal / medical / scientific verification | `strict` |
| Compliance reporting, audit-grade | `paranoid` |

If you find yourself getting too many refusals in `strict` or `paranoid`, the answer is usually one of:

1. **Improve retrieval** — most refusals are caused by the right passage not making it to the generator. Tune `top_k_retrieve` and `top_k_rerank` upward.
2. **Recalibrate the verifier on your domain** — the default threshold (0.0562 for Dual NLI) was fit on RAGTruth. Your domain may need different. See [Calibrate threshold](../how-to/calibrate-threshold.md).
3. **Switch from `paranoid` to `strict`** — the 0.9 threshold is intentionally aggressive; only use it when truly necessary.
