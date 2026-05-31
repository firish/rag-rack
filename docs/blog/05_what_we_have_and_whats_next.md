# Everything in verifiable-rag — and what's coming next

*A full tour of what the library does today, and the SOTA techniques on the roadmap.*

---

I've spent the last few months building [`verifiable-rag`](https://github.com/firish/rag-rack), a Python library for document-grounded Q&A with sentence-level citations, NLI verification, and calibrated refusal. The pitch is short: **every shipping "chat with your documents" product stops at chunk-level citations and prompt-conditioned grounding. The research literature has solved sentence-span attribution and post-hoc faithfulness verification. None of it had shipped in a usable library.** That's the gap.

`v0.5` is on PyPI now (`pip install verifiable-rag`), documented at [firish.github.io/rag-rack](https://firish.github.io/rag-rack/), and validated on three published benchmarks (ALCE, RAGTruth, LitQA2). This post is the complete map: every component that's in the box today, and the SOTA things landing in the next few releases.

If you've followed the [ALCE](https://github.com/firish/rag-rack/blob/main/blog/02_constrained_citations.md), [RAGTruth](https://github.com/firish/rag-rack/blob/main/blog/03_verified_rag.md), or [LitQA2](https://github.com/firish/rag-rack/blob/main/blog/04_litqa2_ablation.md) posts, the headline numbers won't repeat here — this is the architectural tour.

---

# Part 1 — What's shipped

The library is a left-to-right pipeline of pluggable components, each defined by a Python `Protocol` so you can swap any of them for your own implementation. Walking the pipeline from PDF to verified Answer:

## Corpus acquisition

You don't have to write your own paper-fetching pipeline. The library ships scripts for the three benchmarks it validates against:

- **`scripts/fetch_litqa2.py`** — fetches the 199-question LAB-Bench LitQA2 dataset from HuggingFace, then downloads the cited papers from arXiv / PubMed / publisher endpoints with retry logic. Resilient to per-paper failures.
- **`scripts/fetch_alce.py`** — pulls Princeton's ALCE-data archive with the three pre-retrieved-passage sub-benchmarks (ASQA, QAMPARI, ELI5).
- **`scripts/fetch_faithfulness_benches.py`** — downloads RAGTruth, HaluBench, and (when ungated) FaithBench parquet files in one shot.

For your own corpora, anything that produces PDFs works. Local files, S3, HTTP — all that matters is they're parseable.

## Parsing — spans tracked through every layer

Two parsers ship today:

- **`DoclingParser`** — IBM's Docling stack. Best layout fidelity, OCR-capable, slow.
- **`PyMuPDFParser`** — fast, text-only fallback. ~50× faster on PDFs that don't need OCR.

Plus two wrappers that compose with either:

- **`CompositeParser`** — try primary, fall back on failure. The default for robust ingest pipelines (Docling primary, PyMuPDF fallback).
- **`CachingParser`** — content-hashed JSON cache. Re-parsing the same PDF is free after the first pass; matters a lot during eval iteration.

Every parser preserves character-level spans through the entire output. A `Sentence` in the resulting `Document` carries its exact `(doc_id, char_start, char_end, optional bboxes)` — the span never gets lost downstream.

## Sentence segmentation

**wtpsplit SaT** (`sat-3l`) for sentence boundary detection. Returns `(text, start, end)` triples where `input[start:end] == text` always holds — verified by round-trip assertions in CI. If the segmenter ever returned text not present in the input, that sentence would be skipped rather than emit a wrong-but-plausible span.

## Chunking — parent-child with optional Contextual Retrieval

**`ParentChildChunker`** is the default — paragraph-grouped child chunks (default ~400 tokens) that each carry their source `section_id`, `paragraph_id`, and full `sentence_ids` tuple. Chunks NEVER span sections. The "parent" context is computed on demand at generation time by `ParentExpander`, which can return the full section or a configurable window of nearby paragraphs.

Why parent-child? Retrieve with small precise chunks (better recall), generate with expanded parent context (more for the LLM to work with), cite by sentence_id (sentence-precise grounding). Three axes, decoupled.

**`ContextualChunker`** wraps any base chunker to add Anthropic's [Contextual Retrieval](https://www.anthropic.com/news/contextual-retrieval) recipe — LLM-generated context preambles prepended to each chunk before embedding. Configurable granularity: `section` (cheapest — one preamble per Section), `paragraph` (finer), or `chunk` (Anthropic's original recipe — most specific but ~30× the per-doc LLM cost).

Plus a power-user `group_by` callable that lets you cluster by any function (custom topic detection, header level, speaker in transcripts, function in code).

## Embedding — local or hosted, your call

Three embedders behind the same `Embedder` Protocol:

- **`SentenceTransformerEmbedder`** — defaults to `BAAI/bge-small-en-v1.5` (384-dim, ~140 MB, runs anywhere). The local default.
- **`CohereEmbedder`** — Cohere `embed-english-v3.0` (1024-dim, hosted). The published `hybrid_balanced` baseline uses this.
- **`VoyageEmbedder`** — Voyage embeddings (hosted). Cleanest path to long-context embeddings if you're trying late chunking later.

## Indexing — hybrid by default

**`HybridIndex`** combines a dense store (`LanceDBIndex`, file-backed, no server) and a sparse store (`BM25Index` via `bm25s`) with **RRF fusion**. Top-K candidates per sub-index, fused by rank-reciprocal blending. No separate vector-DB service to operate.

LanceDB persists to disk as a directory; BM25 is in-memory with serialization support. Multi-process ingest is supported (commit is serialized behind a lock; prepare is parallelizable).

## Reranking

Two rerankers, same Protocol:

- **`BGERerankerV2`** — local, ~568 MB, runs on CPU/GPU/MPS.
- **`CohereReranker`** — hosted `rerank-v3`. Slightly stronger on most benchmarks; used in the published baseline.

Reranking is optional. `local_minimal` skips it; every other preset includes it.

## Generation — three citation modes

Three generators, all producing `list[CitedSentence]` (text + `supporting_sentence_ids` + confidence):

- **`PromptedCitedGenerator`** — the baseline. Prompts the LLM to emit cites inline by sentence ID. Works with any LiteLLM model (Anthropic, OpenAI, Gemini, Groq, Ollama, vLLM, you name it).
- **`ConstrainedCitedGenerator`** ⭐ — ReClaim-style schema-forced JSON output. The LLM is forced into a structured schema where `cite_ids` come from an enum of valid IDs from the retrieved chunks. No invented IDs are possible at decode time. **The library's default**, and the configuration that achieves the published 0.875 mc_acc on LitQA2 and +4–7 F1 lift on ALCE.
- **`SAFECitedGenerator`** — SAFE-style atomic-claim decomposition. Each sentence is decomposed into atomic factoid claims, each gets its own cite. For domains where multi-claim sentences are common (legal, scientific narrative).

All three integrate with **LiteLLM** for provider-agnostic routing — Anthropic, OpenAI, Gemini, Groq, Together, Ollama (local), vLLM endpoints, all reachable via a model-id string.

## Verification — the headline differentiator

This is the part that justifies "verifiable" in the name. Four concrete verifiers:

- **`HHEMVerifier`** — Vectara's HHEM-2.1-open (~600M params, T5-based NLI). Strong on QA-style entailment.
- **`MiniCheckVerifier`** — Liyan Tang's MiniCheck-Flan-T5-Large (~770M). Strong on structured-data-to-text claims where HHEM is weak.
- **`LLMJudgeVerifier`** — LLM-as-judge via LiteLLM. Strict but expensive. Anthropic prompt caching enabled by default on system + premise so per-doc cost stays sane.
- **`DualNLIVerifier`** ⭐ — HALT-RAG-style ensemble combining two NLI scorers via min / mean / max aggregation. The published RAGTruth baseline shows it matches Sonnet 4.6 LLM-judge at AUROC 0.844 vs 0.846 — **at roughly 1/250th the per-call cost.**

Plus the supporting pieces:

- **`EnsembleScorer`** — generic N-scorer composition (lets you build triple ensembles, etc.).
- **`NLIVerifier`** — generic adapter wrapping any `NLIScorer` into a `Verifier`-protocol class. Lets you use `LLMJudgeVerifier` or `MiniCheckVerifier` directly as the Pipeline verifier.
- **`ModalHHEMScorer` / `ModalMiniCheckScorer`** — for benchmark runs at scale, drop-in GPU-hosted variants that run on Modal T4s without touching your local machine.

The verifier produces a `VerificationResult` per generated sentence: `is_supported: bool`, `nli_score: float`, `claim_text`. The Pipeline acts on the boolean.

## Strictness slider — calibrated refusal

Four strictness modes that map to honest faithfulness thresholds:

| Strictness | Threshold | Behavior |
|---|---|---|
| `loose` | 0.0 | Never refuse. Verifier output is informational only. |
| `balanced` ⭐ | 0.5 | Refuse below 0.5 after surgical correction. Default. |
| `strict` | 0.7 | Refuse below 0.7. Only confident answers slip through. |
| `paranoid` | 0.9 | Refuse below 0.9. High refusal rate; high-trust use cases. |

The Pipeline applies **surgical correction** when the verifier flags individual sentences — they're removed from the answer, the rest is kept, and the `unsupported_claims` list tracks what was dropped. If everything fails verification, the whole answer is hard-refused with a `refusal_reason`.

This is architecturally enforced. The library refuses to claim it verified something it didn't — `strict` and `paranoid` modes raise if no verifier is configured. No prompt-conditioned "say I don't know" fallback.

## Audit trail — programmatic + visual

Every `Answer` ships its full audit trail:

**Programmatic** — convenience accessors that wrap the raw data:

```python
answer.text                          # final answer
answer.sentences                     # list[CitedSentence]
answer.verification_results          # list[VerificationResult]
answer.retrieved_chunks              # passages the generator saw

answer.supported_sentences           # filtered to passed-verification
answer.unsupported_sentences         # filtered to flagged
answer.verification_for(idx)         # lookup by sentence index
answer.cited_sentence_ids            # frozenset of source IDs cited
answer.min_nli_score                 # worst-case sentence
answer.audit_trail()                 # JSON-serializable dict for logs / metrics
```

**Visual** — `answer.to_html()` produces a self-contained HTML report with:

- The query and the answer with inline citation links
- Per-sentence verification color coding (unsupported = red dashed underline)
- Faithfulness card row (overall + retrieval + NLI components)
- Per-sentence verification table with NLI scores
- The reranked passage cards, anchored so citations link in

No JavaScript, no external dependencies, no server needed. Open the file in any browser.

## Calibration tooling

Default thresholds (HHEM 0.3, Dual NLI 0.0562) are calibrated on RAGTruth-train. For your domain, **`scripts/compute_calibrated_metrics.py`** sweeps the threshold on a held-out train slice, freezes it, and applies it to test — producing the publishable calibrated F1 alongside threshold-independent AUROC and AUPRC.

The same script works for single verifiers and ensembles. Specify a list of `LABEL:TRAIN_JSONL:TEST_JSONL` triples and an aggregation method.

## Eval harness

Three benchmark loaders and runners ship in `verifiable_rag.eval`:

- **`RAGTruthBench`** — word-span hallucination annotations on real RAG outputs.
- **`LitQA2Bench`** — 199 multi-choice biomedical scientific Q&A questions with linked papers.
- **`ALCEBench`** — Princeton's three sub-benchmarks (ASQA, QAMPARI, ELI5) with pre-retrieved passages.

Plus **`HarryPotterMicroBench`** — a 29-question hand-curated micro-benchmark on a local PDF, for sanity smokes that don't require external data.

Each benchmark has a dedicated runner that handles ingest, retrieval, generation, verification, and metrics. The metrics module computes set-based citation precision/recall, span tightness, coverage, localization accuracy, and abstention F1 at the sentence level. RAGAS wrappers exist for chunk-level comparisons.

## Configuration — three tiers

**1. Presets** for the common cases:

```python
verifiable_rag.local_minimal()         # BGE + Haiku, no verifier
verifiable_rag.local_verified()        # + HHEM NLI
verifiable_rag.hybrid_balanced()       # ⭐ Cohere + Dual NLI + constrained
verifiable_rag.hybrid_strict()         # refuse below 0.7
verifiable_rag.hybrid_paranoid()       # Sonnet + refuse below 0.9
verifiable_rag.llm_judge_verified()    # Sonnet 4.6 as the verifier
```

**2. YAML** for production:

```python
pipeline = Pipeline.from_yaml("pipeline.yaml")
```

Component types are registered via a public registry (`@register("embedder", "my_custom")`); `registered_types()` enumerates everything the YAML loader understands.

**3. Direct construction** for full control.

## One-liner

For the simplest case — single shot, single doc, single question:

```python
import verifiable_rag
answer = verifiable_rag.ask(
    "What did the authors find?",
    docs="paper.pdf",
    output_html="audit.html",
)
```

Three lines from `pip install` to a verified, cited, browser-viewable answer.

## Bundled demo doc

A small public-domain document about penicillin ships with the package (~50 KB, parsed and cached). Lets you run the examples and verify the install works without finding your own PDF:

```python
from verifiable_rag.demo import sample_paper_path
answer = verifiable_rag.ask("Who discovered penicillin?", docs=sample_paper_path())
```

---

# Part 2 — What's planned

Eight features I think the library should have within the next few minor releases. Each is something that **either no production Python RAG library does well**, or where the SOTA technique hasn't been operationalized into a coherent open-source package.

## HyDE — Hypothetical Document Embeddings

Gao et al. 2022. Instead of embedding the query directly, generate a hypothetical *answer* with an LLM, embed that, and retrieve against the hypothetical-answer embedding. Reported retrieval gains of 10–20% on zero-shot domains.

Why it's interesting: the query is often a poor match for the chunks that contain the answer. The hypothetical answer is in the same "shape" as the source content, so embedding similarity is more meaningful. Especially powerful for technical / scientific domains where queries and answer-passages use different vocabulary.

What we'd build: a `HyDERetriever` wrapper around the existing `HybridIndex` that adds an LLM step before the embedding lookup. Cost is one extra LLM call per query (cheap with Haiku + caching). Plumbing-only, no new model dependencies.

## Late chunking (Jina, 2024)

Embed the full document at once with a long-context embedder, *then* chunk the resulting token-level embeddings. Each chunk's embedding is computed while the model can see the rest of the document — preserves cross-sentence context inside the embedding itself.

Why it's interesting: it's the opposite of Contextual Retrieval, addressing the same fundamental problem (chunk embeddings losing document context) from the other direction. Zero LLM calls; just requires a long-context embedder (Jina v3, Voyage long-context, Cohere embed-multilingual-v3).

What we'd build: a `LateChunkingEmbedder` that takes a `Chunker` + a long-context embedder, runs the document through end-to-end, then pools by chunk boundaries. Will require pinning a specific long-context embedder; Voyage v3 looks like the right target.

## Sentence-level dual NLI

Today's `DualNLIVerifier` combines per-pair scores from two scorers and produces a single response-level faithfulness signal. HALT-RAG's actual recipe operates at the sentence level — combine each sentence's two scores, then aggregate across sentences.

Why it's interesting: response-level aggregation hides which specific sentences failed which specific verifier. Sentence-level dual exposes the per-claim, per-model decision matrix, which is the richest data for audit and for downstream metric design.

What we'd build: a runner that stores per-sentence scores from each scorer (not just per-response), plus a new aggregation strategy in `EnsembleScorer` that operates at sentence level. Expect a small lift on RAGTruth's published F1 number; bigger lift on audit explainability.

## Streaming citations

Generate the answer token-by-token, emit each cite as soon as the schema completes it. The user sees citations appear in real-time, the same way ChatGPT streams text.

Why it's interesting: this is the UX bar set by every chat-style product, and verifiable-rag is the only library that *can* stream citations because they're emitted alongside text by the constrained generator. We just don't expose it yet.

What we'd build: `Pipeline.stream_ask(query)` returning an async generator of `CitedSentence` objects as they're decoded. The verifier runs after the stream completes. Requires LiteLLM streaming support, which exists.

## LAQuer — localized attribution queries

Wadhwa & Sundararajan, ACL 2025. User highlights a span in the generated output, system returns the minimal source span that supports it. Inverse of citation — the user picks the claim, the system finds the evidence.

Why it's interesting: it's the most direct UX answer to "wait, where does this come from?" without requiring users to read the audit trail. Especially compelling for legal / medical / scientific verification workflows.

What we'd build: a `localize_query(answer, user_span)` API that takes the user's selection, walks the citation graph, and returns the tightest supporting source span. Integration would land in the HTML audit report as a click-to-highlight behavior; the underlying logic is small.

## ColBERTv2 via RAGatouille

Token-level late interaction. Each query token is matched against each chunk token independently, then aggregated. ColBERTv2 generally outperforms single-vector dense retrieval, especially on out-of-domain corpora.

Why it's interesting: it's a categorically different retrieval shape that complements the dense+sparse hybrid we ship today. RAGatouille has done the operational work to make it usable; integrating it as another `DenseIndex` implementation is the unblocking step.

What we'd build: a `ColBERTIndex` implementing the same Protocol as `LanceDBIndex`. Storage shape differs (token-level vs document-level), but the Pipeline doesn't have to know.

## Cross-document disagreement detection

When multiple sources are cited for the same claim and they *disagree*, flag it. Today the library would happily cite two sources making contradictory statements and report `is_supported=True` for the cite count.

Why it's interesting: in any setting where the corpus mixes primary literature with editorials (legal, medical literature reviews, news aggregation), source disagreement is the failure mode that hurts users most. No library handles this.

What we'd build: a `disagreement_check(answer)` post-processing step that compares cited spans pairwise via NLI for contradiction (separate from entailment). Adds a new `disagreements` field to `Answer`. Probably uses the existing dual NLI verifier with a contradiction-direction prompt rather than entailment.

## Visual citation highlighting in the PDF viewer

The audit HTML report shows passage cards. The natural next step: render the actual source PDF inline, with bounding boxes drawn around the cited spans. The library already tracks bbox per Span when the parser provides them (Docling does).

Why it's interesting: this is the NotebookLM UX move that makes citation feel concrete — see the actual highlighted paragraph in the actual paper, not a text excerpt in a card. It's purely a rendering problem; the spans are already tracked.

What we'd build: integration with [`react-pdf-viewer`](https://react-pdf-viewer.dev/) for the JS side, plus a `to_pdf_viewer_overlay(answer, pdf)` helper on the Python side. Lands first as a Hugging Face Space; later as an embeddable component.

## Honorable mentions (further out)

- **Self-RAG** — model decides *when* to retrieve, *what* to retrieve, *what* to cite. Cuts retrieval calls for queries the model already knows.
- **Bespoke-MiniCheck-7B and Patronus Lynx-8B / 70B** as Tier-2 NLI options for users who can afford bigger models — adds ~3–5 F1 points on RAGTruth at 10× the inference cost.
- **MMR diversity** in retrieval — `MMRReranker` that maximizes marginal relevance instead of pure score, reducing chunk redundancy in the top-K.
- **Calibration wizard** — interactive CLI for fitting verifier thresholds on user-labeled data. Today it's a script; would be smoother as `verifiable_rag.calibrate(my_examples)`.
- **FaithBench / HaluBench cross-validation** — once FaithBench is un-gated on HF, run the same dual-NLI vs Sonnet-judge comparison and publish the second-benchmark validation.
- **Open-weights local generators via vLLM** — for the air-gapped use case. Today you can use Ollama, but vLLM is the higher-throughput option for self-hosted production.

---

# Where to start

If you've read this far and want to play with it:

```bash
pip install verifiable-rag
export ANTHROPIC_API_KEY=...
```

```python
import verifiable_rag
from verifiable_rag.demo import sample_paper_path

answer = verifiable_rag.ask(
    "What is the mechanism of action of penicillin?",
    docs=sample_paper_path(),
    output_html="audit.html",
)
print(answer.text)
# Open audit.html for the full audit trail
```

Five lines. No API keys beyond Anthropic for the generator. Bundled doc means no PDF needed for the first run.

If you find the audit-trail HTML page interesting — that's the differentiator. Open it, click a citation, see exactly which source span supports the claim, see which sentences the verifier flagged. That's what "verifiable RAG" actually looks like.

Docs at [firish.github.io/rag-rack](https://firish.github.io/rag-rack/) cover concepts (architecture, citation flow, verification, strictness), how-to guides (use HHEM, calibrate threshold on your domain, integrate observability, swap LLM provider, local-only setup), and the full API reference.

Three published benchmark reports validate the architecture: [ALCE](https://github.com/firish/rag-rack/blob/main/benchmarks/PUBLISHED_alce.md) (citation generation), [RAGTruth](https://github.com/firish/rag-rack/blob/main/benchmarks/PUBLISHED_ragtruth.md) (faithfulness verification), [LitQA2](https://github.com/firish/rag-rack/blob/main/benchmarks/PUBLISHED_litqa2.md) (end-to-end). Every number can be reproduced from the commands in the report.

If you have a use case the library doesn't cover yet — or a SOTA technique I should be looking at — open an issue on [GitHub](https://github.com/firish/rag-rack). Roadmap priorities are shaped by what real users ask for.

---

*verifiable-rag is MIT-licensed. The benchmark reports under [`benchmarks/`](https://github.com/firish/rag-rack/tree/main/benchmarks) are the audit trail for everything I publish here. Methodology critiques welcome — eval rigor is the whole moat, and the only way to find the holes is to invite people to look for them.*
