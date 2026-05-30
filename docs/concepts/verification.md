# Verification

The headline differentiator: every generated sentence gets fact-checked against the source span it cites, by a fast small-model NLI ensemble that matches a frontier LLM judge.

## The two-tier interface

The library distinguishes two related abstractions:

| Protocol | Method | Used by |
|---|---|---|
| `NLIScorer` | `score_pairs(pairs) → list[float]` | RAGTruth runner, ensemble composition |
| `Verifier` | `verify(sentences, documents) → list[VerificationResult]` | The Pipeline |

A `Verifier` builds `(premise, hypothesis)` pairs from `CitedSentence` + `Document` and feeds them to an `NLIScorer`. Most concrete classes (`HHEMVerifier`, `DualNLIVerifier`) implement both — they can be used either as a Pipeline verifier or as a raw scorer for benchmark runners.

```python
# As a Pipeline verifier
pipeline = Pipeline(..., verifier=DualNLIVerifier(HHEMVerifier(), MiniCheckVerifier()))

# As a raw scorer for benchmark scoring
from verifiable_rag.eval.ragtruth_runner import run_ragtruth
report = run_ragtruth(DualNLIVerifier(HHEMVerifier(), MiniCheckVerifier()), bench)
```

## Built-in verifiers

### `HHEMVerifier` — single small NLI model

Vectara's HHEM-2.1-open (~600M params, T5-Flan-Large backbone). Trained on summarization-style entailment.

```python
from verifiable_rag.verifiers import HHEMVerifier

verifier = HHEMVerifier(threshold=0.3)  # default threshold
```

- **Strengths:** Very strong on QA-style entailment (factoid claims against retrieved passages). RAGTruth AUROC 0.81.
- **Weaknesses:** Weak on data-to-text claims (Yelp records → narrative). RAGTruth Data2txt AUROC 0.57.

### `MiniCheckVerifier` — single small NLI model

Liyan Tang's MiniCheck-Flan-T5-Large (~770M params). Trained on synthetic claim decompositions, multi-domain.

```python
from verifiable_rag.verifiers import MiniCheckVerifier

verifier = MiniCheckVerifier()
```

- **Strengths:** Better than HHEM on structured-data-to-text claims (RAGTruth Data2txt AUROC 0.70).
- **Weaknesses:** Slightly worse than HHEM on QA, slower at inference.

### `DualNLIVerifier` ⭐ — the recommended default

Combines two scorers via min/mean/max aggregation. The published baseline.

```python
from verifiable_rag.verifiers import DualNLIVerifier, HHEMVerifier, MiniCheckVerifier

verifier = DualNLIVerifier(
    HHEMVerifier(),
    MiniCheckVerifier(),
    aggregation="min",   # HALT-RAG convention: any scorer flagging = flag
    threshold=0.0562,    # RAGTruth-train-calibrated default
)
```

- **AUROC: 0.844 on RAGTruth (vs 0.846 for Sonnet judge)**
- **Per-call cost: ~$0.0004 (vs ~$0.05 for Sonnet)**
- **F1: 0.706 calibrated on held-out test**

Why dual beats single: HHEM and MiniCheck have **complementary blind spots**. HHEM's training distribution doesn't cover Data2txt; MiniCheck's does. Ensembling at the `min` aggregation flags an example if either scorer says unsupported — net effect is the union of "either model caught it."

[Full RAGTruth result →](https://github.com/firish/rag-rack/blob/main/benchmarks/PUBLISHED_ragtruth.md)

### `LLMJudgeVerifier` — LLM-as-judge fallback

For comparison and "ceiling" use cases. Uses LiteLLM to route to any chat LLM. Anthropic prompt caching enabled by default on system + premise.

```python
from verifiable_rag.verifiers import LLMJudgeVerifier

verifier = LLMJudgeVerifier(
    model="anthropic/claude-sonnet-4-6",
    max_workers=8,           # ThreadPoolExecutor for concurrent calls
    temperature=0.0,
    num_retries=2,
)
```

- **Strengths:** Best-quality single model. Useful as a benchmark ceiling.
- **Weaknesses:** ~250× higher per-call cost than Dual NLI. API rate limits. Bursty failures under load.

Most production deployments shouldn't use this as the primary verifier. The Dual NLI matches it on RAGTruth; reserve LLM-judge for offline eval and adversarial testing.

## Aggregation strategies

`DualNLIVerifier` and `EnsembleScorer` support three aggregations:

| Aggregation | Per-pair behavior | Use case |
|---|---|---|
| `min` ⭐ | flag if *any* scorer says unsupported | **Default** — HALT-RAG convention, most sensitive |
| `mean` | average the scores | Smoother — for calibration where bimodal scores hurt |
| `max` | flag only if *all* scorers say unsupported | Lenient — high precision, lower recall |

The published RAGTruth result uses `min`. Switch to `mean` if your scorer outputs are noisy and the `min` aggregation flags too aggressively.

## How verification fits in the Pipeline

When the Pipeline runs `answer = pipeline.ask(query)`:

1. Generator produces `cited_sentences: list[CitedSentence]`
2. **If a verifier is configured**, it produces `verification_results: list[VerificationResult]`
3. The Pipeline applies **strictness-controlled filtering**:
    - `loose`: every generated sentence is returned (verification is informational)
    - `balanced` / `strict` / `paranoid`: sentences with `is_supported=False` are **surgically removed**; if the resulting answer's faithfulness score drops below the strictness threshold, the whole answer is **refused**
4. The remaining sentences become `answer.sentences`; the dropped ones become `answer.unsupported_claims`

See the [strictness concept page](strictness.md) for the threshold table.

## Calibration

The default thresholds (HHEM 0.3, Dual NLI 0.0562) are fit on RAGTruth-train. **They are not guaranteed to be optimal for your domain.**

If your inputs are different (legal contracts, medical notes, code documentation), you should re-fit the threshold on a small labeled validation set from your domain. The library ships a calibration script:

```bash
python scripts/compute_calibrated_metrics.py \
    --verifier "DualNLI:my_train_scores.jsonl:my_test_scores.jsonl" \
    --slug my_domain_calibrated
```

[Full calibration walkthrough →](../how-to/calibrate-threshold.md)

## What verification *can't* do

- **It can't catch citation-cite mismatches that the verifier itself was trained to accept.** If the NLI model was trained on summarization data and you're verifying scientific claims, edge cases may slip through.
- **It can't validate facts outside the cited span.** If the LLM emits "Penicillin was discovered in 1928" and the cited source span only says "in the late 1920s," the NLI model probably accepts it. Strict factuality requires post-hoc fact-checking against a knowledge base, which is out of scope.
- **It can't fix bad retrieval.** If the right source passage was never retrieved, the verifier can only flag the generator's output as unsupported — it can't reach back into the corpus to find the missing evidence.

These limits are why the audit trail matters: every published number comes with its caveats; every Answer ships its full decision path so reviewers can spot the holes.

## The benchmark that validates this

[RAGTruth](https://github.com/firish/rag-rack/blob/main/benchmarks/PUBLISHED_ragtruth.md) is the canonical 2,700-example RAG hallucination corpus (Niu et al., NAACL 2024). Our calibrated numbers:

| Verifier | AUROC | F1 (calibrated) | Per-call cost |
|---|---|---|---|
| HHEM | 0.813 | 0.663 | ~$0.0002 |
| MiniCheck | 0.836 | 0.696 | ~$0.0002 |
| **Dual NLI (HHEM + MC)** | **0.844** | **0.706** | ~$0.0004 |
| Sonnet 4.6 judge | 0.846 | 0.707 (on 300-ex subset) | ~$0.05 |

Dual NLI matches Sonnet on both AUROC and calibrated F1, at ~250× lower per-call cost. **This is the result that justifies the library's design.**
