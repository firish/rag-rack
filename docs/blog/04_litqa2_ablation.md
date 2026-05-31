# Five levers, one ceiling: a LitQA2 ablation

*I tried two retrieval techniques and three generator architectures on LitQA2. Here's what moved the needle, what didn't, and where the ceiling actually is.*

---

I've been building [`verifiable-rag`](https://github.com/firish/rag-rack) — a Python library for document-grounded Q&A with sentence-level citations and post-hoc faithfulness verification. The library has a working baseline on [LitQA2](https://github.com/Future-House/LAB-Bench) (FutureHouse's 199-question biomedical scientific Q&A benchmark) at **mc_accuracy 0.870** — slightly above PaperQA2's reported ~0.85.

But I wanted to push past it. The natural question: *where's the headroom?* Is it retrieval, generation, citation, or something else? Five hypotheses, each tied to a SOTA technique:

1. **Better retrieval — Contextual Retrieval** (Anthropic 2024): prepend LLM-written context preambles to each chunk before embedding.
2. **Better generator — constrained decoding** (ReClaim, ACL 2024): schema-force the LLM to emit valid citation IDs from an enum per sentence.
3. **Better citations — SAFE** (May 2025): decompose each sentence into atomic-claim factoids and cite each one independently.

I ran a 3×2 ablation (three generators × two retrieval configurations) on a 29-question stratified slice. The TL;DR up front:

> **The biggest lever is the generator (constrained > prompted by ~7 points on the pilot, ~0.5 on the full corpus). Contextual retrieval doesn't help — retrieval isn't the bottleneck. SAFE matches constrained on MC accuracy but doesn't move localization, which suggests the localization ceiling is benchmark-imposed, not generator-imposed.**

Below: how I ran it, what each lever actually did, and what the result means for anyone building a RAG system.

---

## The baseline

For context, here's the pipeline that gets to 0.870:

- **Parsing:** Docling (with PyMuPDF fallback) on 185 biomedical papers
- **Chunking:** ParentChildChunker — small child chunks (max 400 tokens) with section/paragraph pointers
- **Retrieval:** Hybrid — BM25 + Cohere embed-english-v3 dense, fused with RRF
- **Reranking:** Cohere rerank-v3 (top 100 retrieve → top 10 rerank)
- **Generation:** Claude Haiku 4.5 with prompt-based citation ("emit cites inline by sentence ID")
- **Citation matching:** Three-tier (exact / bold / fuzzy) on the LitQA2 multi-choice options

Full setup is in [`benchmarks/PUBLISHED_litqa2.md`](https://github.com/firish/rag-rack/blob/main/benchmarks/PUBLISHED_litqa2.md). Sit-down number: **mc_accuracy 0.870** on all 199 questions, **0.875** with constrained decoding swapped in (the v11 variant).

The interesting numbers underneath the headline, though, are these:

| Metric | Value | Reading |
|---|---|---|
| `citation_precision` | 0.83 | When the generator emits a cite, it's right 83% of the time |
| `citation_recall` | 0.47 | Only 47% of gold-supporting sentences get cited |
| `coverage` | 0.76 | 24% of generated sentences come out uncited |
| `localization_accuracy` | 0.24 | Of cites that "support" the answer, only 24% point at the *exact* gold sentence (the others land in the right *chunk*) |

That last number is the one I most wanted to push up. 0.24 means the model is finding the right region of the right paper but missing the right sentence three-quarters of the time. If you're building a system that needs precise grounding (legal, medical, scientific), localization is the metric that matters.

---

## What I tried

The 3×2 grid:

|  | no contextual retrieval | section-level CR |
|---|---|---|
| `prompted` generator | baseline | + CR on top |
| `constrained` generator | ReClaim-style | both new |
| `safe` generator | atomic claims | (deferred — first measure CR's effect on prompted/constrained) |

Concretely:

- **Contextual Retrieval** wraps the existing chunker. For each chunk, an LLM (Haiku) writes a 50–100 token preamble describing what the chunk is about within the document, and the preamble gets prepended before embedding. Section-level granularity (one preamble per Section, shared across child chunks under it) keeps the cost reasonable — ~$15 for full LitQA2 vs ~$300 if we contextualized per child chunk. Anthropic reports ~67% reduction in retrieval failures with this; I wanted to measure it on my benchmark.
- **Constrained generation** uses LiteLLM `response_format` to force the LLM into a JSON schema: an array of `(sentence_text, cite_ids[])` where `cite_ids` are drawn from an enum of available sentence IDs from the retrieved chunks. No invented IDs, no missing cites.
- **SAFE generation** extends constrained with atomic-claim decomposition: each sentence is broken into atomic factoid claims, each claim gets its own cite. Designed to lift localization specifically.

All runs used the same model (Haiku 4.5), same retrieval (Cohere embed + BM25 + Cohere rerank, top 100 → top 10), same delay (6s), same first-30-questions-with-PDFs slice (29 effective).

---

## Results

Side-by-side on the same 29 questions:

| Metric | prompted | prompted + CR | **constrained** | constrained + CR | SAFE |
|---|---|---|---|---|---|
| **mc_accuracy** | 0.897 | 0.897 | **0.966** | **0.966** | **0.966** |
| mc_correct / wrong / unanswered | 26 / 0 / 3 | 26 / 0 / 3 | 28 / 0 / 1 | 28 / 0 / 1 | 28 / 0 / 1 |
| citation_precision | **0.828** | 0.828 | 0.672 | 0.672 | 0.652 |
| citation_recall | 0.472 | 0.475 | 0.484 | 0.484 | **0.496** |
| **citation_f1** | 0.463 | 0.466 | 0.466 | 0.466 | **0.475** |
| coverage | 0.759 | 0.759 | 0.793 | 0.793 | 0.793 |
| **localization_accuracy** | **0.241** | 0.241 | 0.207 | 0.207 | 0.207 |
| abstention_f1 | 0.000 | 0.000 | **1.000** | 1.000 | 1.000 |

Five things this table tells you:

### 1. Contextual retrieval is a null result on LitQA2

Across both generator backbones, adding section-level CR moved literally nothing. Not MC accuracy. Not citation_precision. Not citation_recall. Not coverage. Not localization. The retrieval was already strong enough that adding document-level context preambles to the chunk embeddings didn't change which chunks made it through retrieval, which chunks the reranker picked, or which sentences the generator cited.

I expected at least *some* movement — Anthropic's published results showed -67% retrieval failures across their evals. It didn't happen here. The most plausible explanation: a hybrid retrieval stack (sparse BM25 + dense Cohere embed + cross-encoder rerank) is already doing the job that CR is supposed to do, and the marginal value of an LLM-written preamble disappears in the noise.

**Implication:** before spending compute on Contextual Retrieval for your own RAG system, measure where your retrieval errors actually are. If your hybrid+rerank stack is saturating on the questions where the gold passage *can* be found, CR won't help.

### 2. Constrained generation is the biggest single lever

Going from `prompted` to `constrained` picked up 2 of the 3 previously-unanswered questions, lifting MC accuracy from 0.897 to 0.966 on this slice — **+6.9 pp**. The published full-corpus delta is smaller (+0.5 pp from v9 to v11), so the pilot number is partly small-sample-flattering. But the direction is robust and matches what we saw on ALCE (constrained beat prompted by 4–7 F1 points there too).

Why this works: schema-forced output gives the model fewer ways to wimp out. Prompted output has an easy escape hatch ("I can't determine this from the passages") which the model takes on borderline cases. Constrained schema requires the model to pick from the enum or emit a specific "insufficient information" option. On borderline cases, the schema commits the model and it usually picks correctly.

Side effect: citation_precision drops (0.83 → 0.67) because the schema enforces 1–3 cites per sentence, widening the cite net to include some wrong cites. Localization drops slightly for the same reason. **citation_f1 stays roughly constant** — the recall gain ≈ the precision loss. So constrained is the right pick if MC accuracy matters; prompted may still be right for high-precision audit use cases.

### 3. SAFE matches constrained on MC, edges it on citation_f1, doesn't move localization

SAFE gets exactly the same MC accuracy as constrained (0.966), with a slightly better citation_f1 (0.475 vs 0.466) thanks to higher recall (0.496 vs 0.484). The atomic-claim decomposition spreads cites across more sentences, picking up a few extra gold supports per response.

But: **localization didn't move at all** (0.207 vs 0.207). SAFE was *designed* specifically to lift localization — each atomic claim gets its own tightly-scoped cite. If that doesn't help here, something else is bounding localization.

### 4. The localization ceiling is benchmark-imposed, not generator-imposed

This is the most interesting finding. After running three SOTA generators (one purpose-built for citation specificity, one purpose-built for localization), localization is identical for the two schema-enforced variants at 0.207, and slightly *higher* for the prompted baseline at 0.241.

That last fact is the giveaway. The "best" localization on LitQA2 belongs to the *least specific* generator architecture. That can't be a generator problem — it's a scoring artifact. What's happening: schema-enforced generators emit *more* cites per claim, and LitQA2's localization metric penalizes the broader cite net even when the additional cites are *also* correct. The metric is implicitly preferring single-cite output even when multi-cite is more informative.

**This is a benchmark limit, not a system limit.** To actually validate sentence-level localization, you need a benchmark scoring at the *atomic-claim level* (RAGTruth, FaithBench) — which is exactly what those benchmarks exist for, and what SAFE was designed against. LitQA2's sentence-level multi-choice gold can't differentiate between SAFE's tight-but-many cites and prompted's loose-but-few.

### 5. The pilot doesn't extrapolate cleanly to the full corpus

The 29-question slice scores ~3 pp higher than the full 199-question corpus across the board (prompted gets 0.897 here vs 0.870 published; constrained gets 0.966 vs 0.875 published). The first 30 questions are evidently the easier ones in the LitQA2 ordering, so absolute numbers don't transfer. But *relative ordering and direction* should: contextual retrieval being null on the easy slice is consistent with no benefit on harder ones; constrained beating prompted is consistent with the published +0.5 pp.

---

## Recommendations

For LitQA2-style RAG systems (factoid scientific Q&A with multi-choice scoring):

1. **Ship constrained decoding as the default.** It's the lever that actually moves MC accuracy, and the precision regression is acceptable for most use cases. The library defaults to `ConstrainedCitedGenerator` for this reason.
2. **Don't ship Contextual Retrieval for this workload.** The infrastructure is built (the library exposes `ContextualChunker(granularity="section"/"paragraph"/"chunk")`), but for a saturated hybrid retrieval stack on factoid QA, it's a $15 no-op. Other workloads — large heterogeneous corpora, ambiguous queries, hallucination-detection — may benefit. Measure first.
3. **For localization-sensitive use cases, change benchmarks.** If your application needs sentence-precise citations (legal, medical, scientific verification), measure on a benchmark with sentence-level (or atomic-claim-level) faithfulness gold. LitQA2's MC scoring is the wrong metric to drive that work.

```python
from verifiable_rag import Pipeline
from verifiable_rag.chunkers import ParentChildChunker
from verifiable_rag.generators import ConstrainedCitedGenerator

pipeline = Pipeline(
    parser=...,
    chunker=ParentChildChunker(max_child_tokens=400),
    embedder=...,  # Cohere or BGE
    indexer=...,   # HybridIndex(dense + BM25)
    reranker=...,  # Cohere or BGE rerank
    generator=ConstrainedCitedGenerator(model="anthropic/claude-haiku-4-5"),
)
```

That's the configuration that gets the published 0.875 on the full LitQA2 test corpus.

---

## Honest caveats

**The pilot is 29 questions, not 199.** The 2×2 retrieval ablation (CR vs no CR) is robust on this slice — every metric was bit-identical between the two configurations, which is a strong null signal. But I haven't run CR on the full 192-paper corpus, only the easy 29-question slice. If you want full-corpus CR numbers, expect to spend ~$15 + ~3 hours of API time. Given the bit-identical null on the pilot, I'm not personally going to spend that.

**The localization ceiling is interpreted, not measured.** I'm claiming that LitQA2's metric structure caps localization at ~0.24 — that's an inference from three generators all hitting roughly the same number, not a formal proof. A cleaner test would be a synthetic dataset with sentence-precise gold + adversarial multi-cite generators, to show that even with perfect cites, the metric saturates.

**Anthropic API stability was an issue.** The constrained+CR cell of the 2×2 took three attempts to complete cleanly — Anthropic's `overloaded_error` 529s hit during the high-burst contextualization phase even with throttled concurrency. The final clean run used `max_workers=3` and `num_retries=5` on the contextualizer; previous attempts with default 8 workers + 2 retries dropped 12-19 questions per run. The library now defaults to the conservative settings.

**Pilot sampling.** First-30-questions-with-PDFs isn't a stratified random sample. The slice scores 3 pp higher than the full corpus across the board, suggesting it's easier-than-average. Direction of effect should still transfer; absolute numbers don't.

---

## What's next

LitQA2 is one of three published benchmarks in the library — the others are [ALCE](https://github.com/firish/rag-rack/blob/main/blog/02_constrained_citations.md) (citation generation) and [RAGTruth](https://github.com/firish/rag-rack/blob/main/blog/03_verified_rag.md) (post-hoc faithfulness verification, where a dual NLI ensemble matches a frontier LLM judge at 1/250th the cost).

The natural next direction is HyDE for query enhancement, late chunking with long-context embedders, and visual citation highlighting — see [the feature roadmap post](https://github.com/firish/rag-rack/blob/main/blog/05_what_we_have_and_whats_next.md) for what's in the library today and what's planned next.

If you'd find this kind of library useful — span-grounded citations, calibrated NLI verification, refusal-when-uncertain — drop a star on [the repo](https://github.com/firish/rag-rack) or open an issue with your use case.

The library is [`verifiable-rag` on GitHub](https://github.com/firish/rag-rack) — MIT-licensed, on PyPI (`pip install verifiable-rag`), docs at [firish.github.io/rag-rack](https://firish.github.io/rag-rack/). The benchmark reports under [`benchmarks/`](https://github.com/firish/rag-rack/tree/main/benchmarks) are the audit trail for everything I post about — every published number can be reproduced from the commands listed there.

Methodology critiques welcome. The whole moat is eval rigor; the only way to find the holes is to invite people to look for them.
