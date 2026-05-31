# Verified RAG: every sentence checked

*How a 600M + 770M NLI ensemble matches Claude Sonnet at hallucination detection on RAGTruth — at 1/250th the per-call cost.*

---

I've been building [`verifiable-rag`](https://github.com/firish/rag-rack) — a Python library for document-grounded Q&A that produces sentence-level citations and verifies every claim against its cited span. The pitch is that the system either answers truthfully or refuses; it does not generate plausible-sounding nonsense.

That pitch only holds if the verifier is good. So I spent the last week running calibrated benchmarks on RAGTruth — the 18K-example canonical hallucination-detection corpus — to figure out **what actually works for production-grade faithfulness verification**.

The headline finding:

> **A dual ensemble of two small NLI models (HHEM-2.1-open + MiniCheck-Flan-T5-Large, combined via min aggregation) matches Claude Sonnet 4.6's hallucination-detection quality on RAGTruth — at roughly 1/250th the per-call cost.**

That number deserves an asterisk for sample-size reasons I'll get into. But the direction is clear and reproducible: cheap, open-source NLI verifiers are within striking distance of frontier LLM judges on the metric people actually care about (response-level hallucination F1), and they're already there on AUROC.

Below: how I got there, what surprised me, what the production recommendation is, and where it breaks.

---

## Why this matters (skip if you live in RAG land)

Every shipping "chat with your documents" product (NotebookLM, ChatPDF, Humata, Adobe Acrobat AI) stops at chunk-level citations and prompt-conditioned grounding. The model is told to cite its sources; in practice, ~10–15% of the time it cites something irrelevant or just fabricates plausible nonsense (see NotebookLM's own published numbers).

The 2024–2026 research literature has solved the underlying problem twice over:

- **Span-level attribution** — ReClaim (ACL 2024), SAFE (May 2025), LAQuer (ACL 2025) all show how to make every generated sentence carry a tight pointer to the source span that entails it.
- **Post-hoc faithfulness verification** — small NLI models like Vectara's HHEM-2.1-open and Liyan Tang's MiniCheck can fact-check claims at inference time and flag the unsupported ones.

None of it has shipped in a usable library. The gap I'm filling.

But "verify every claim with an NLI model" has been a known recipe for a while. The unsolved practical question is **which NLI model, and what does it actually buy you over the easy alternative (just ask GPT-4)?** Especially given that LLM-as-judge is by far the most common production pattern today.

That's what the benchmark answers.

---

## The benchmark — RAGTruth, calibrated

[RAGTruth](https://huggingface.co/datasets/wandb/RAGTruth-processed) (Niu et al., NAACL 2024) is the canonical RAG-hallucination corpus. It ships ~18K LLM responses across three tasks (QA, Data-to-text, Summary) from six generating LLMs (GPT-3.5/4, Llama-2-7B/13B/70B, Mistral-7B), each with word-level human annotations marking which spans are hallucinations.

For verification testing, each example is `(context, response, gold_hallucination_spans)`. The verifier's job is binary: given the context and the LLM-generated response, was the response hallucinated or clean? I report response-level F1, AUROC, and AUPRC.

**Methodology that matters:** every threshold I report is fit on a held-out **train split** and applied to **test**. The "in-sample best F1" numbers (which you'll see in some papers) are an upper bound, not what you should expect in production — and they were typically only 0.5–1pp higher than my calibrated numbers in my runs, so the discipline cost was small.

---

## What the verifiers actually are

Three flavors, all behind the same `NLIScorer` interface (one method: `score_pairs(pairs: list[tuple[str, str]]) -> list[float]`):

1. **HHEM-2.1-open** (Vectara, ~600M params, T5-Flan-Large backbone). Trained on summarization-style entailment. The closest thing to a "default" small NLI verifier in the open-source ecosystem.
2. **MiniCheck-Flan-T5-Large** (Liyan Tang et al. 2024, ~770M params). Trained on synthetic claim decompositions across multiple domains. Different training distribution from HHEM.
3. **LLM-as-judge** (Claude Haiku 4.5, Claude Sonnet 4.6). Per-claim prompt: "is this claim entailed by this passage?" → structured JSON output.

I ran each verifier on the full RAGTruth test split (2700 examples) where compute allowed, fit the threshold on a stratified subset of train (1500 examples for the NLI models, 300 for the LLM judges due to API cost), and reported calibrated test-set F1.

Sentence-level: each response gets segmented into sentences with [wtpsplit](https://github.com/segment-any-text/wtpsplit), the verifier scores each `(context, sentence)` pair independently, and the response-level score is the **min** across sentences. The convention: any unsupported sentence flags the whole response. This is the HALT-RAG (Sept 2025) approach.

---

## The headline result

| Verifier | n_test | AUROC | **Calibrated F1** | Per-call cost |
|---|---|---|---|---|
| HHEM single | 2700 | 0.813 | 0.663 | ~$0.0002 |
| MiniCheck single | 2700 | 0.836 | 0.696 | ~$0.0002 |
| **Dual NLI (HHEM + MC, min)** | 2700 | **0.844** | **0.706** | ~$0.0004 |
| **Sonnet 4.6 judge** | 300 | **0.846** | **0.707** | ~$0.05 |
| Triple (HHEM + MC + Sonnet) | 300 | 0.861 | 0.734 | ~$0.05 |

Dual NLI: AUROC 0.844, F1 0.706.
Sonnet judge: AUROC 0.846, F1 0.707.

Statistically indistinguishable on either metric. The Sonnet number has a wider CI because it's on 300 examples instead of 2700 (cost reasons — running Sonnet on the full test was going to be ~$50). But the direction is clear.

**Adding Sonnet on top as a third ensemble member buys you another ~2 F1 points** (0.706 → 0.734) on the 300-example subset where all three scored. Real lift, but only worth it if you've already accepted LLM-judge costs for other reasons.

---

## What surprised me: complementarity

The interesting story isn't the headline number — it's *why* the ensemble works.

The two NLI models were trained on different distributions, and it shows in the per-task breakdown:

| Task | HHEM AUROC | MiniCheck AUROC | Sonnet AUROC |
|---|---|---|---|
| **QA** (MS MARCO + retrieved passages) | **0.874** | 0.839 | 0.844 |
| **Summary** (CNN/DailyMail) | 0.759 | 0.777 | 0.848 |
| **Data2txt** (Yelp records → narrative) | **0.566** | 0.702 | 0.852 |

HHEM is **great at QA** — that's its training distribution. Factoid claims against retrieved passages are exactly what summarization-entailment models see during training.

HHEM is **bad at Data2txt** — AUROC 0.566 is barely better than random. Turning a structured Yelp record into prose requires a different kind of entailment check (does this narrative actually correspond to the structured fields?) that HHEM was never trained on.

MiniCheck **fills exactly this gap.** Its synthetic-claim-decomposition training covers structured→narrative inferences. Data2txt AUROC jumps from 0.566 (HHEM alone) to 0.702 (MiniCheck alone) to 0.685 (the dual). The dual loses a tiny bit on Data2txt vs MiniCheck-alone because HHEM's bad scores drag the min down — but gains across the board everywhere else.

**This is the textbook case for an ensemble.** Two models with different blind spots, neither dominant. Min aggregation (HALT-RAG convention: "any model says unsupported → flag") performed best in my runs, but mean is within 0.005 AUROC and gives smoother per-example confidence scores if you care about calibration.

Why the two NLI models can collectively keep up with Sonnet: Sonnet is uniformly good across tasks (AUROC 0.844–0.852, near-flat) but it's not *better-than-best* on any single task. HHEM beats Sonnet on QA, MiniCheck nearly ties on Summary. When you compose HHEM and MiniCheck through their strong tasks, you get a verifier that's at-or-above frontier on aggregate.

---

## What you'd actually ship

```python
from verifiable_rag import Pipeline
from verifiable_rag.verifiers import DualNLIVerifier, HHEMVerifier, MiniCheckVerifier

pipeline = Pipeline(
    parser=...,
    generator=...,
    verifier=DualNLIVerifier(
        HHEMVerifier(),
        MiniCheckVerifier(),
        aggregation="min",
        threshold=0.0562,   # fit on RAGTruth-train — re-fit on your domain if it differs
    ),
)

pipeline.ingest("paper.pdf")
answer = pipeline.ask("What did the authors find?")

# Verification results are aligned by cited_sentence_index back into answer.sentences.
result_by_idx = {vr.cited_sentence_index: vr for vr in answer.verification_results}
for i, sentence in enumerate(answer.sentences):
    vr = result_by_idx.get(i)
    if vr and not vr.is_supported:
        # Downstream UI: render unsupported badge, surface vr.nli_score, etc.
        print(f"FLAGGED: {sentence.text!r} (nli={vr.nli_score:.2f})")
```

That's the production configuration. Both NLI models download lazily from HuggingFace on first call (~1.4 GB total, cached forever afterward). After that there's no per-call cost — they run on whatever CPU/GPU you have. On a Modal T4, scoring 2700 RAGTruth responses cost me about 25 cents.

For comparison, the equivalent Sonnet judge run would cost ~$50 and require an Anthropic API key. The Haiku judge would cost ~$7. Both keep ticking up with every query in production.

The default threshold (0.0562) was fit on RAGTruth train with min aggregation. **It will not be optimal for every domain.** If you have a different distribution of contexts (legal contracts, medical literature, code), fit your own threshold with the included calibration script — it takes ~50 lines of labeled data and one command.

---

## The honest caveats

**The Sonnet comparison is on 300 examples, not 2700.** Same stratification (100 per task) and same seed, so the comparison is methodologically clean, but the CI on Sonnet's AUROC is wider (±0.045 vs ±0.015 for the dual). I'm confident in "dual matches Sonnet" as a directional claim; I'm not confident the gap is *exactly* 0.002. The right-side caveat: Sonnet may genuinely be ~3 points better in expectation than this benchmark shows. Even then, the cost-quality tradeoff still strongly favors the dual.

**Haiku-as-judge does not calibrate well on small samples.** I tried it (Haiku 4.5, 300 train, 600 test) and the train-fit threshold collapsed to a knife-edge that didn't transfer — calibrated F1 fell to 0.14 from an in-sample 0.66. The mechanism is real: RAGTruth train has a 46% hallucination base rate vs test's 35%, and Haiku's confidence distribution is near-bimodal (most claims either obviously supported or obviously not). With 300 train examples that combination found a degenerate threshold. Fix: either more train data or a different operating-point criterion (balanced accuracy instead of F1). I'm flagging this as future work; for now Haiku-judge is in the "in-sample exploratory" bin in my published numbers, not the "production-ready" bin.

**RAGTruth is just one benchmark.** The dual matching Sonnet on RAGTruth doesn't guarantee it matches Sonnet on FaithBench, HaluBench, or your domain's hallucinations. FaithBench is currently HF-gated; HaluBench cross-validation is on the backlog.

**Threshold transfer is sensitive to base rate.** Train (46% hall) and test (35% hall) have meaningfully different base rates in RAGTruth. The optimal F1-maximizing threshold depends on base rate, so applying a train-fit threshold to a different-base-rate test introduces some bias. A base-rate-aware calibration (e.g. optimize at fixed precision, or use balanced accuracy) would be more rigorous. The honest takeaway: the published F1 numbers are within a couple of points of the true value, but they're not precise to the third decimal.

---

## What this means if you're building a RAG system

Three concrete takeaways:

1. **Don't use a frontier LLM as your default hallucination judge.** It's wildly expensive per call, and on at least one well-tested benchmark a $0.0004 open-source ensemble matches its quality. Save the LLM judge for offline eval and adversarial testing, not real-time verification.

2. **Don't use one NLI model — use two.** HHEM alone leaves Data2txt-style outputs basically uncovered. The two models compose to a verifier that's robust across the task distributions you'll see in practice. Cost-wise the second model is "free" in the sense that it doesn't add per-call money, just a one-time download.

3. **Calibrate on labeled data, not vibes.** The in-sample best-F1 threshold and the train-fit threshold differ by 1–2 F1 points in my measurements — small but not zero. Reporting in-sample numbers is the most common rigor failure I see in RAG eval; don't do it.

`DualNLIVerifier` ships as the library's recommended default. The full benchmark report (with per-model breakdowns, reproducibility instructions, and source numbers) lives at [benchmarks/PUBLISHED_ragtruth.md](https://github.com/firish/rag-rack/blob/main/benchmarks/PUBLISHED_ragtruth.md). The library is [`verifiable-rag` on GitHub](https://github.com/firish/rag-rack) — MIT-licensed, on PyPI (`pip install verifiable-rag`), docs at [firish.github.io/rag-rack](https://firish.github.io/rag-rack/).

---

## What's next

The natural follow-ups are sentence-level NLI ensembling (currently response-level), HyDE for query enhancement, late chunking with long-context embedders, and visual citation highlighting in the audit report — see [the feature roadmap post](https://github.com/firish/rag-rack/blob/main/blog/05_what_we_have_and_whats_next.md) for the full list of what's in the library today and what's planned for the next few releases.

If you'd find this kind of library useful — span-grounded citations, calibrated NLI verification, refusal when the system can't ground the answer — drop a star on [the repo](https://github.com/firish/rag-rack) or open an issue with your use case. Roadmap priorities get shaped by real users.

---

*verifiable-rag is MIT-licensed and on PyPI (`pip install verifiable-rag`). Documentation at [firish.github.io/rag-rack](https://firish.github.io/rag-rack/). For the citation-generation half of the story (constrained decoding vs prompted on ALCE), see [the companion post](https://github.com/firish/rag-rack/blob/main/blog/02_constrained_citations.md). Methodology critiques welcome — eval rigor is the whole moat.*

*Find me on [X](https://x.com/) / [GitHub](https://github.com/firish/rag-rack). Eval rigor is the whole moat — if you spot a methodology hole, I want to hear about it.*
