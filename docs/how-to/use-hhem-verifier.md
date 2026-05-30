# Use the HHEM verifier

This guide walks through three ways to use [HHEM-2.1-open](https://huggingface.co/vectara/hallucination_evaluation_model) — Vectara's small NLI model — as the faithfulness verifier in your pipeline.

## Single HHEM verifier (lighter than dual)

For pipelines that don't need the Dual NLI ensemble (smaller install, faster inference, or you've calibrated HHEM specifically on your domain):

```python
from verifiable_rag import Pipeline
from verifiable_rag.verifiers import HHEMVerifier
# ... other components

pipeline = Pipeline(
    # ...
    verifier=HHEMVerifier(threshold=0.3),  # default threshold
    strictness="balanced",
)
```

Or via a preset that already wires it for you:

```python
from verifiable_rag import local_verified
pipeline = local_verified()  # uses HHEM by default
```

## Tweaking the threshold

The default threshold of `0.3` was empirically chosen because HHEM was trained on tight summarization-style entailment data, but generators produce paraphrased / synthesized cited sentences that legitimately score in the 0.3–0.6 range.

Raise the threshold for stricter behavior:

```python
HHEMVerifier(threshold=0.5)
```

Lower it for more permissive behavior:

```python
HHEMVerifier(threshold=0.15)
```

For a principled choice, [calibrate on your own labeled data](calibrate-threshold.md).

## Picking the device

HHEM uses transformers under the hood and respects device placement:

=== "Auto (default)"

    ```python
    HHEMVerifier()  # uses the default device (CPU unless transformers picks differently)
    ```

=== "CPU"

    ```python
    HHEMVerifier(device="cpu")
    ```

=== "Apple Silicon (MPS)"

    ```python
    HHEMVerifier(device="mps")
    ```

=== "NVIDIA (CUDA)"

    ```python
    HHEMVerifier(device="cuda")
    ```

Long premises (>2K tokens) can OOM on MPS at large batch sizes — the attention layer's softmax tensor is the bottleneck. If you hit memory errors, reduce the batch size in your runner config or switch to CPU.

## As a raw NLI scorer

`HHEMVerifier` also implements the `NLIScorer` protocol — you can call it directly without the Pipeline:

```python
from verifiable_rag.verifiers import HHEMVerifier

scorer = HHEMVerifier()
scores = scorer.score_pairs([
    ("Penicillin was discovered in 1928.", "Penicillin was first identified in 1928."),
    ("Cats are mammals.", "The moon is made of cheese."),
])
# scores → [0.92, 0.04] approximately
```

This is what the [RAGTruth runner](https://github.com/firish/rag-rack/blob/main/scripts/run_ragtruth.py) uses internally.

## Inside a Dual NLI ensemble

The recommended production use is HHEM paired with MiniCheck in a `DualNLIVerifier`:

```python
from verifiable_rag.verifiers import DualNLIVerifier, HHEMVerifier, MiniCheckVerifier

verifier = DualNLIVerifier(
    HHEMVerifier(),
    MiniCheckVerifier(),
    aggregation="min",
    threshold=0.0562,  # RAGTruth-train calibrated
)
```

See [Verification](../concepts/verification.md) for why dual beats single, and the [RAGTruth benchmark report](https://github.com/firish/rag-rack/blob/main/benchmarks/PUBLISHED_ragtruth.md) for the numbers.

## When NOT to use HHEM

- **Your domain is wildly different from summarization-style entailment.** HHEM was trained on news summarization data; if you're verifying claims about code, legal contracts, or structured data, MiniCheck is often stronger.
- **You need maximum portability.** HHEM ships ~600 MB of weights from HuggingFace on first use. For air-gapped deployments, consider `LLMJudgeVerifier` with a local LLM endpoint.
- **You don't care about per-call cost.** If LLM API spend is fine for your use case and you want the strongest single signal, `LLMJudgeVerifier(model="anthropic/claude-sonnet-4-6")` is the ceiling.

For most use cases, the answer is "use the Dual NLI ensemble" — it matches Sonnet judge quality at 1/250× the cost.
