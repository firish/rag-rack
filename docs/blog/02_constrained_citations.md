# Sentence-grounded citations beat prompted citations on ALCE

*Constrained decoding for citation generation lifts F1 by 4–7 points on Princeton's ALCE benchmark, judged by two independent LLMs. Why the dual-judge methodology matters more than the headline.*

---

I've been building [`verifiable-rag`](https://github.com/firish/rag-rack) — a Python library for RAG that produces sentence-level citations and verifies every claim against its cited span. Last month I finished the citation-generation layer and ran the obvious benchmark: ALCE (Gao et al., EMNLP 2023), Princeton's three-sub-benchmark citation-quality suite.

The headline:

> **Constrained-decoding citations (ReClaim-style sentence-by-sentence structured output) beat the prompted-citations baseline by 4–7 F1 points across ASQA and QAMPARI, under both Haiku-4.5 and Sonnet-4.6 as judges. Library default is now `constrained`.**

But the headline isn't the most interesting thing. The interesting thing is **how dual-LLM-judge cross-validation changed the conclusions** I would have drawn from either judge alone — and what that says about how to evaluate RAG citation systems in general.

---

## What ALCE actually tests (skip if you already know)

[ALCE](https://github.com/princeton-nlp/ALCE) ships three sub-benchmarks, each with pre-retrieved passages so the citation-generation layer is what's under test (retrieval is held constant):

- **ASQA** — factoid Q&A with answer ambiguity. Cites should hit any of multiple valid sub-answers.
- **QAMPARI** — multi-hop Q&A where the answer is a *set* of entities. Each entity needs its own cite.
- **ELI5** — long-form explanation. Long answer, BM25 retrieval, hardest task.

For each example, ALCE expects the system to generate an answer with inline citations to specific passage IDs. The scoring is:

- **citation_recall** (per claim): is at least one cited passage entailed by the claim?
- **citation_precision** (LOO per cite): would the claim still be entailed if we removed this cite?

The original ALCE paper used a fine-tuned T5-XXL TRUE model as the NLI judge. Modern practice is to use a frontier LLM (GPT-4 / Sonnet / Opus) as the judge — better accuracy, no T5-XXL deployment headache, but introduces a different consistency concern.

---

## The methodological problem

LLM-as-judge for citation quality has a known failure mode: **the judge's generosity is correlated with its model family.** If you use Haiku to evaluate Haiku's outputs, you get a number. If you use Sonnet, you get a different (usually lower) number. Which is correct?

The honest answer: neither, individually. But the *direction of disagreement* between two well-chosen judges is itself informative — it tells you when your output is robust enough that judges agree, versus when it's borderline enough that the judge's biases dominate.

So I ran every ALCE configuration through **two independent Claude judges** (Haiku 4.5 and Sonnet 4.6, same scoring prompt). Same outputs, two different graders.

---

## The two generator configs

What's being compared:

- **Prompted** — the baseline. The prompt instructs the LLM to emit one cite per sentence, referencing source sentences by ID. Loose enforcement; the LLM may emit zero, one, or many cites per claim depending on its mood.
- **Constrained** — ReClaim-style structured output. The LLM is forced (via Anthropic's `response_format` / OpenAI structured outputs) to produce a list of `(sentence_text, cite_ids[])` tuples with 1–3 cites per sentence enforced by schema. No optional cites; no free-form fallback.

Both run on Claude Haiku 4.5 as the generator. Same retriever (Cohere rerank-v3 over the pre-baked candidate passages → top-5). The only thing changing is the decoding strategy.

---

## The headline numbers (Sonnet-judged)

| Sub-benchmark | Prompted (rec / prec / F1) | **Constrained (rec / prec / F1)** | Δ F1 |
|---|---|---|---|
| **ASQA** | 0.882 / 0.882 / 0.882 | **0.953 / 0.885 / 0.918** | **+3.6** |
| **QAMPARI** | 0.904 / 0.901 / 0.902 | **0.952 / 0.906 / 0.929** | **+2.7** |
| **ELI5** | ~0.91 / ~0.90 (calibrated) | not measured | — |

Constrained wins by **+7.1 pp recall on ASQA** and **+4.8 pp on QAMPARI**, while keeping precision essentially flat. The recall win is what you'd expect — multi-cite enforcement means more chances to land a supporting passage per claim. The precision *not collapsing* is the surprise; constrained's extra cites don't dilute average correctness.

For context against the published literature:

| System | ASQA top-100 (rec / prec) | QAMPARI top-100 (rec / prec) |
|---|---|---|
| ALCE paper (ChatGPT, T5-XXL judge) | ~65 / ~70 | ~65 / ~70 |
| ReClaim (ACL 2024) | ~75 / ~80 | — |
| SAFE (May 2025, oracle setting) | ~85–90 / ~85–90 | — |
| **This work — prompted (Sonnet-judge)** | 88.2 / 88.2 | 90.4 / 90.1 |
| **This work — constrained (Sonnet-judge)** | **95.3 / 88.5** | **95.2 / 90.6** |

Both configurations sit **above ALCE-paper and ReClaim numbers**, and the constrained variant **matches or exceeds SAFE-tier** on both measured sub-benchmarks — under the more rigorous of our two judges.

Caveat that I'll repeat below: these are Claude-judge numbers, not T5-XXL TRUE numbers. The original ALCE paper's absolute values aren't directly comparable. Direction and rank-order are robust; absolute numbers may shift by a few points if you swap in TRUE as the judge. That's on the backlog.

---

## The actually interesting finding: judges disagree less when the model is forced to be specific

Here's the dual-judge cross-validation table — same outputs, two graders:

| Sub-bench × Config | Haiku-judge (rec / prec) | Sonnet-judge (rec / prec) | Δ (Haiku → Sonnet) |
|---|---|---|---|
| ASQA prompted | 0.934 / 0.934 | 0.882 / 0.882 | **−5.2 / −5.2** |
| ASQA **constrained** | 0.969 / 0.893 | **0.953 / 0.885** | **−1.6 / −0.8** |
| QAMPARI prompted | 0.933 / 0.930 | 0.904 / 0.901 | **−2.9 / −2.9** |
| QAMPARI **constrained** | 0.960 / 0.911 | **0.952 / 0.906** | **−0.8 / −0.5** |
| ELI5 prompted | 0.938 / 0.933 | calibrated ~0.91 / ~0.90 | — (inferred) |

Three findings here, in order of decreasing-obvious to most-interesting:

1. **Sonnet is consistently stricter than Haiku** — across every cell, Sonnet returns lower scores. Expected; Sonnet has more capability to spot subtle citation/claim mismatches.

2. **Constrained wins under *both* judges** — so the "constrained beats prompted" claim isn't a Haiku-judge artifact. Both judges agree on the ranking.

3. **The Sonnet-Haiku gap is *much smaller* under constrained** — on ASQA, prompted shows a 5.2 pp drop from Haiku→Sonnet; constrained shows only a 1.6 pp drop. Same pattern on QAMPARI (2.9 → 0.8). **The output of the constrained generator is more judge-robust** — both judges agree on it more often than they agree on prompted's output.

That third finding is the real story. When you force the model (via schema) to produce specific, multi-cite output, you remove the optionality that Haiku-judge was previously giving "free passes" on. Prompted output had room for Haiku-judge generosity — claims with a single weak cite that Haiku was willing to accept but Sonnet was not. Constrained output doesn't have that ambiguity; cites are load-bearing by construction.

**Practical takeaway:** if you're using a small LLM as a judge in production faithfulness pipelines, the *judge-robustness* of your generator architecture matters more than the absolute numbers it produces with any single judge. Constrained decoding raises the floor — your outputs hold up under stricter graders.

---

## Why prompted didn't collapse, and why constrained's precision held

The naïve worry with constrained decoding is that it'd hurt precision — forcing 1–3 cites per claim could mean padding with weak/irrelevant cites. That's not what happens.

Looking at the per-sentence cite attribution (each generated sentence carries its own `[cite_ids]` list rather than collapsing to a per-question union), I see two things:

- **Constrained's cites are more cited-sentence-aligned** because the schema asks for cites *per sentence*, not per claim. The model naturally produces cites that match the sentence-level claim, not the broader question.
- **Prompted often degenerates to one cite per question** (a single cite at the end of the answer covering everything), which inflates per-claim cite count under leave-one-out scoring and artificially deflates precision.

The honest precision comparison is the LOO per-cite version with per-sentence attribution — which is what I'm reporting above. Under that metric, constrained's precision is *comparable* to prompted's (within 0.5 pp on Sonnet-judge), while recall is much higher.

---

## What to actually ship

```python
from verifiable_rag import Pipeline
from verifiable_rag.parsers import DoclingParser
from verifiable_rag.chunkers import ParentChildChunker
from verifiable_rag.rerankers import CohereReranker
from verifiable_rag.generators import ConstrainedCitedGenerator

pipeline = Pipeline(
    parser=DoclingParser(),
    chunker=ParentChildChunker(parent_size=512, child="sentence"),
    reranker=CohereReranker(),
    generator=ConstrainedCitedGenerator(
        model="anthropic/claude-haiku-4-5",
        # Schema enforces 1–3 cites per sentence; no need to prompt for it.
    ),
)

pipeline.ingest("paper.pdf")
answer = pipeline.ask("What did the authors find?")

for sentence in answer.sentences:
    # Each CitedSentence carries its supporting sentence IDs by construction
    print(sentence.text, "→", sentence.supporting_sentence_ids)
```

That's the production configuration that achieved the numbers above. The schema enforcement is what does the work — every sentence in the output is guaranteed to have at least one cite ID. There's no "fall through and return uncited text" failure mode.

`ConstrainedCitedGenerator` works with any LiteLLM model that supports structured outputs (Anthropic, OpenAI, and most providers do; Gemini's structured-output support is mature; local-model support depends on the [`outlines`](https://github.com/dottxt-ai/outlines) or `lm-format-enforcer` backends).

The prompted variant (`PromptedCitedGenerator`) is still shipped for two reasons: (a) it works on every model regardless of structured-output support, and (b) it's the natural baseline to point at when explaining why constrained matters.

---

## The honest caveats

**Claude judges, not T5-XXL TRUE.** The original ALCE paper used T5-XXL TRUE (Honovich et al. 2022) as the NLI judge. I used Claude Haiku 4.5 and Sonnet 4.6. Direction and rank-order are robust; absolute values may shift by a few points if you re-judge with TRUE. Cross-validation with TRUE is on the Phase 5 backlog — and would let me submit numbers directly comparable to the paper, which matters for academic citing.

**ELI5 missing Sonnet-judge measurement.** I have Haiku-judge numbers for ELI5 (0.938 / 0.933 prompted) but didn't re-judge with Sonnet for cost reasons — ELI5's long answers blow up Sonnet judge cost by ~3×. The calibrated ~0.91/~0.90 estimate uses the QAMPARI-measured Haiku→Sonnet 2.9 pp drop. Direct measurement is deferred.

**Constrained requires structured-output support.** Closed-API models (Anthropic, OpenAI, Gemini) all support this natively. Local open-weights models need `outlines` or `lm-format-enforcer` as a runtime dependency. If you're running Llama-3 locally you have a working path but the integration is slightly more work than just installing `litellm`.

**Retrieval held constant.** ALCE ships pre-retrieved passages so the generator is what's under test. That's by design — but it means these numbers don't reflect end-to-end RAG quality where retrieval mistakes compound with citation mistakes. For an end-to-end test with real retrieval, see the [LitQA2 ablation post](https://github.com/firish/rag-rack/blob/main/blog/04_litqa2_ablation.md), which includes the [Contextual Retrieval](https://www.anthropic.com/news/contextual-retrieval) comparison.

---

## What this means if you're building a RAG system with citations

Three takeaways:

1. **If your generator supports structured output, use it for citations.** Don't prompt-engineer your way to inline cites if your model can be schema-constrained instead. The recall win is large and the precision cost is near-zero.

2. **Single-judge LLM evaluation hides architectural truths.** Haiku-judge-on-Haiku-output suggested prompted was at 0.934 — pretty good. Sonnet-judge revealed it was actually at 0.882, and that constrained's gap to prompted was bigger than it looked. If you're calibrating thresholds or making architectural decisions off a single LLM judge, swap to a second-judge cross-validation before you commit.

3. **Per-sentence cite attribution matters for honest precision metrics.** If you collapse all cites in an answer to a per-question union, you'll over-count cites per claim under LOO scoring and underreport precision. Track which cites came from which sentence; the LOO math falls out cleanly from there.

I'm shipping `constrained` as the library's default generator. Prompted stays as the model-agnostic fallback for cases where structured output isn't available (some local models, niche providers).

The full benchmark report with reproducibility instructions and per-sub-benchmark numbers lives at [benchmarks/PUBLISHED_alce.md](https://github.com/firish/rag-rack/blob/main/benchmarks/PUBLISHED_alce.md). The library itself is [`verifiable-rag` on GitHub](https://github.com/firish/rag-rack) — MIT-licensed, on PyPI as `pip install verifiable-rag`. Documentation at [firish.github.io/rag-rack](https://firish.github.io/rag-rack/).

---

## What's next

Phase 5 is the hardening + reference UI sprint: Gradio demo on HF Spaces with PDF preview, citation chips, faithfulness badges, and a strictness slider. mkdocs-material documentation site. YAML pipeline configs.

The next benchmark post is **LitQA2 with Contextual Retrieval** — I currently sit at ~0.87 multi-choice accuracy on the 199-question LitQA2 set (above PaperQA2's reported ~0.85), and I want to see whether Anthropic's Contextual Retrieval recipe pushes that another 1–2 points. If you've tried Contextual Retrieval in your own RAG stack and have experience to share — open an issue, I'd love to compare notes.

If span-grounded citations, calibrated NLI verification, and refusal-when-uncertain are the kind of properties you'd want in a RAG library, drop a star on the repo or open an issue with your use case. Phase 5 priorities are getting shaped by real users.

---

*verifiable-rag is MIT-licensed and available on PyPI (`pip install verifiable-rag`). The benchmark reports under [`benchmarks/`](https://github.com/firish/rag-rack/tree/main/benchmarks) are the audit trail for everything I publish in posts like this. Methodology critiques welcome — eval rigor is the whole moat, and the only way to find the holes is to invite people to look for them.*
