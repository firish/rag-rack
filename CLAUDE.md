# CLAUDE.md

This file gives Claude Code (and any other AI assistant) the full context needed to be productive on this project. Read it end-to-end before suggesting changes.

---

## 1. Project at a glance

**Working name:** `verifiable-rag` (rename before public launch)

**One-line:** A Python library for document-grounded Q&A that produces sentence-level citations and verifies every claim against its cited span — so the system either answers truthfully or refuses.

**Why this exists:** The "chat with your documents" space is crowded, but ~every shipping product (NotebookLM, ChatPDF, Humata, Adobe Acrobat AI, Kotaemon, AnythingLLM, etc.) stops at chunk-level citations and prompt-conditioned grounding. The 2024–2026 research literature has solved sentence-span citation, post-hoc faithfulness verification, and calibrated abstention — but none of it has shipped in a usable library. That's the gap.

**Audience:** Developers, ML researchers, and tool builders who need RAG they can audit. Not end users (yet).

**Distribution:** GitHub + PyPI. Reference Gradio UI on Hugging Face Spaces. Hosted product is explicitly out of scope until library traction is proven.

---

## 2. Core thesis (do not drift from this)

A verifiable RAG library is differentiated when it does all of these together:

1. **Span-level citations** — every generated sentence carries `(supporting_sentence_ids, confidence)` linked back to exact source spans with `(doc_id, page, char_span, bbox)`.
2. **Architectural hard refusal** — refusal is enforced by faithfulness thresholds, not just a "say I don't know" prompt.
3. **Post-hoc faithfulness verification** — every claim gets NLI-checked against its cited span.
4. **Calibrated abstention** — combining retrieval score, generation log-probs, and NLI score into a `faithfulness_confidence`, with a user-tunable strictness slider.
5. **Auditability** — users can inspect retrieval ranking, reranker decisions, and per-claim verification.

If a change to the codebase doesn't strengthen one of these five, ask whether it should be in scope at all.

---

## 3. Competitive landscape (so we don't reinvent)

**Closest open-source competitors:**
- **PaperQA2** (FutureHouse) — agentic scientific RAG with reranking + contextual summarization. Superhuman on LitQA2. Strongest baseline for retrieval+citation accuracy. **Library, no UI**, scientific focus, no span-level citations or NLI verification.
- **Kotaemon** (Cinnamon) — best polished OSS UI with PDF preview + chunk highlights. **Chunk-level**, no faithfulness verification.
- **AnythingLLM, RAGFlow, Onyx, Quivr, LocalGPT, h2oGPT** — chunk-level grounding, prompt-conditioned refusal.

**Closest commercial:**
- **NotebookLM** — best UX, passage-chip citations, ~13% hallucination rate (still). Cloud-only, Gemini-only.
- **Adobe Acrobat AI Assistant** — clickable PDF citations but Adobe explicitly disclaims attribution accuracy.
- **Humata, ChatPDF** — chunk citations, weak refusal.

**Research SOTA (the techniques we operationalize):**
- **ReClaim** (ACL 2024) — interleaved reference-claim generation via constrained decoding over a sentence prefix tree. ~90% citation accuracy.
- **SAFE** (May 2025) — in-generation attribution, sentence-by-sentence as it streams. ~95% first-step accuracy.
- **LAQuer** (ACL 2025) — localized attribution queries; user highlights an output span and gets the minimal supporting source span.
- **HALT-RAG** (Sept 2025) — dual-NLI ensemble for faithfulness verification.
- **Contextual Retrieval** (Anthropic, 2024) — chunk preamble before embedding; -67% retrieval failures with reranking.
- **Late Chunking** (Jina, 2024) — embed full document, then chunk the embeddings; preserves long-range context.
- **MiniCheck, HHEM-2.1-open, Bespoke-MiniCheck** — small, fast NLI-style faithfulness models.

The SOTA citation/verification techniques are NOT chunking strategies — they operate at generation/post-generation time. Citation granularity and chunking granularity are decoupled in our architecture.

---

## 4. Architecture overview

The library is a pipeline of pluggable interfaces. Vanilla defaults work out of the box; SOTA techniques are opt-in modules.

```
PDF/EPUB/DOCX
    │
    ▼
┌─────────────┐
│   Parser    │  docling (default) | PyMuPDF | MinerU | ebooklib
└─────┬───────┘  → preserves spans + bboxes
      ▼
┌─────────────┐
│  Document   │  doc_id, sections[], paragraphs[], sentences[]
│   model     │  every sentence: (id, text, page, char_span, bbox)
└─────┬───────┘
      ▼
┌─────────────┐
│   Chunker   │  Recursive (default) | Late chunking | Contextual | Parent-child
└─────┬───────┘  → chunks know which sentence_ids they contain
      ▼
┌─────────────┐
│   Indexer   │  Hybrid: BM25 (bm25s) + Dense (LanceDB)
└─────┬───────┘  → optional: ColBERTv2 via RAGatouille
      ▼
┌─────────────┐
│  Retriever  │  Top-K hybrid with RRF fusion
└─────┬───────┘
      ▼
┌─────────────┐
│  Reranker   │  Cohere rerank-3 | BGE reranker v2 | ColBERTv2
└─────┬───────┘
      ▼
┌──────────────────┐
│ CitedGenerator   │  Modes:
│                  │   - "prompted"     (baseline)
│                  │   - "constrained"  (ReClaim-style, SOTA)
│                  │   - "post_hoc"     (two-pass alignment)
└─────┬────────────┘  → output: sentences[(text, [supporting_sent_ids], conf)]
      ▼
┌─────────────┐
│  Verifier   │  HHEM-2.1-open | MiniCheck | Dual-NLI ensemble
└─────┬───────┘  → per-claim entailment; calibrated faithfulness_confidence
      ▼
┌─────────────────────┐
│  Abstention layer   │  strictness: loose | balanced | strict | paranoid
└─────┬───────────────┘  → "surgical correction" or hard refusal
      ▼
   Final answer
```

### Pipeline API sketch

```python
from verifiable_rag import Pipeline
from verifiable_rag.parsers import DoclingParser
from verifiable_rag.chunkers import ContextualChunker
from verifiable_rag.indexers import HybridIndex
from verifiable_rag.embedders import BGEEmbedder
from verifiable_rag.indexers.sparse import BM25Index
from verifiable_rag.rerankers import CohereReranker
from verifiable_rag.generators import CitedGenerator
from verifiable_rag.verifiers import DualNLIVerifier

pipeline = Pipeline(
    parser=DoclingParser(),
    chunker=ContextualChunker(parent_size=512, child="sentence"),
    indexer=HybridIndex(dense=BGEEmbedder(), sparse=BM25Index()),
    reranker=CohereReranker(),
    generator=CitedGenerator(mode="constrained"),
    verifier=DualNLIVerifier(strictness="strict"),
)

pipeline.ingest("path/to/book.pdf")
answer = pipeline.ask("What does the author say about X?")
# answer.sentences -> [(text, [supporting_sentence_ids], confidence), ...]
# answer.faithfulness_score -> 0.93
# answer.unsupported_claims -> []
```

---

## 5. Build vs. buy decisions

**Use existing libraries (don't reinvent):**

| Layer | Library |
|---|---|
| PDF parsing | docling (primary), PyMuPDF (fallback), MinerU (academic), Nougat (math) |
| EPUB | ebooklib |
| Sentence segmentation | wtpsplit (primary), spaCy senter (fallback) |
| Embeddings | sentence-transformers + BGE-M3 / Voyage-3 / Jina v3 / OpenAI |
| Vector index | LanceDB (file-backed, no server) |
| Sparse retrieval | bm25s |
| Reranker | Cohere rerank-3, BGE reranker v2-m3, ColBERTv2 via RAGatouille |
| LLM routing | LiteLLM |
| Constrained decoding | outlines or lm-format-enforcer (for local models); structured outputs (Anthropic tool use, OpenAI structured outputs) for closed models |
| NLI verifiers | vectara/hallucination_evaluation_model (HHEM-2.1-open), bespokelabs/Bespoke-MiniCheck-7B |
| Eval metrics building blocks | RAGAS, DeepEval |
| Reference UI | Gradio (demo), Next.js + react-pdf-viewer + EPUB.js (later) |

**Build custom (this is the IP):**

1. **Unified `Document` data model** — span-tracking primitives every other layer depends on.
2. **Parent-child chunker** with span preservation (existing splitters drop offsets).
3. **`CitedGenerator`** — three modes (prompted, constrained, post-hoc) with citation-by-sentence-id. **This is the heart of the library.**
4. **`Verifier` orchestration** — atomic claim decomposition, dual-NLI ensemble, calibrated thresholds.
5. **Calibrated abstention layer** — combines retrieval score + generation log-probs + NLI score into a single faithfulness confidence with user-tunable strictness.
6. **Eval harness** — span-level metrics (citation precision/recall, span tightness, abstention F1, localization accuracy) on LitQA2, RAGTruth, FaithBench, HaluBench. **This is half of why anyone trusts the library.**
7. **Pipeline API** — the swap-anything orchestration layer.
8. **Citation-rendering UI components** — span highlights, faithfulness badges, strictness slider.

**Actively resist building:**
- Embedding models, ANN indexes, PDF parsers, NLI models, LLMs, agent frameworks.

**Actively resist using off-the-shelf:**
- LangChain's high-level chains (too opinionated, leak abstractions through citation layer)
- LlamaIndex's `CitationQueryEngine` as more than a baseline reference (not span-grounded)
- Any library that doesn't preserve character offsets through parsing → chunking → retrieval

---

## 6. Hard rules

### Span preservation is non-negotiable
If at any point we can't trace a sentence in an answer back to `(doc_id, page, char_start, char_end, bbox)` in the source, the thesis collapses. Every parser, chunker, and retrieval step MUST preserve offsets. Test this with round-trip assertions in CI.

### Citation granularity ≠ chunking granularity
We may chunk at 512 tokens for retrieval and still emit sentence-level citations. The sentence IDs travel through the chunk metadata. Don't let anyone "simplify" by collapsing these.

### Faithfulness verification is mandatory in `strict` and `paranoid` modes
A verified-mode answer that wasn't actually verified is a bug, not a feature. The verifier must always run; "skip verification" is for `loose` mode only.

### No silent failures in the citation layer
If we can't find supporting sentences for a generated claim, the claim must be flagged or stripped — never returned silently as if cited.

### Eval before optimization
Don't tune chunk sizes, swap embedders, or "improve" anything without running the eval harness. Numbers, not vibes.

---

## 7. Roadmap (16 weeks to v0.5)

Assumes ~15-20 hrs/week. Each phase ends with a public artifact.

### Phase 0 — Foundations (Week 1)
- Repo skeleton: `pyproject.toml`, ruff, pytest, mypy, pre-commit, GitHub Actions CI
- Naming, license, README v0
- Download benchmarks: LitQA2, RAGTruth, HaluBench. Write loaders.
- 1-page design doc (data contracts, Pipeline API, scope for v0.5)
- Identify 1 design partner

**Artifact:** empty repo, design doc, 3 benchmark loaders, smoke tests green.

### Phase 1 — Baseline pipeline (Weeks 2–4)
**Week 2:** `Document` model, `Parser` interface, `DoclingParser`, sentence segmentation. Round-trip span tests.
**Week 3:** `Chunker` (recursive with span preservation), `Embedder` (BGE-small for dev), `Index` (LanceDB), BM25 (bm25s), hybrid with RRF.
**Week 4:** `Generator` (LiteLLM), baseline `PromptedCitedGenerator`, `Pipeline` class. End-to-end demo on 1 PDF. Run on LitQA2; record baseline.

**Artifact:** `pip install -e .` works, baseline numbers logged. **Make repo public.**

### Phase 2 — Eval harness (Weeks 5–6)
**Week 5:** metrics — citation precision/recall, span tightness, abstention F1, localization accuracy. Wrap RAGAS for comparison.
**Week 6:** CLI runner, markdown reports, GitHub Actions eval-on-PR. Comparison table vs. paper-qa, naive RAG.

**Artifact:** `BENCHMARKS.md`. **Blog post #1:** "Building a verifiable RAG library — baseline numbers I'm trying to beat."

### Phase 3 — Sentence-level citation (Weeks 7–9)
**Week 7:** parent-child chunker (paragraph parents, sentence children). Generator cites by sentence_id.
**Week 8:** ReClaim-style constrained decoding. Outlines/lm-format-enforcer for open models; structured outputs for closed.
**Week 9:** post-hoc attribution mode (cross-encoder alignment). Compare three modes on eval.

**Artifact:** sentence-grounded citations in 3 modes. **Blog post #2:** comparison with span tightness numbers and failure cases.

### Phase 4 — Faithfulness verification + calibrated refusal (Weeks 10–12)
**Week 10:** `Verifier` interface. Wrap HHEM-2.1-open and MiniCheck. Atomic claim decomposition.
**Week 11:** dual-NLI ensemble. Calibration on RAGTruth. `faithfulness_confidence` combining retrieval + generation + NLI signals. Strictness slider (`loose` / `balanced` / `strict` / `paranoid`).
**Week 12:** surgical correction mode. Hard refusal mode. Full eval — abstention F1 should jump.

**Artifact:** v0.4 release. **Blog post #3:** "Verified RAG: every sentence checked." Calibration curves, side-by-side examples.

### Phase 5 — Hardening + reference UI (Weeks 13–15)
**Week 13:** YAML pipeline configs, mkdocs-material docs, tutorials, mypy strict.
**Week 14:** Gradio demo with PDF viewer, citation chips, faithfulness badges, strictness slider. Deploy to HF Spaces. 5-min Loom.
**Week 15:** pick 2–3 SOTA modules — late chunking, Contextual Retrieval, ColBERTv2, RAPTOR — depth over breadth.

**Artifact:** v0.5. **Blog post #4 / launch:** "Show HN: verifiable-rag."

### Phase 6 — Launch + listen (Week 16+)
HN, X, r/MachineLearning, r/LocalLLaMA. Awesome-RAG submissions. Watch issues, respond fast for 2 weeks. v0.6 direction based on real user requests.

---

## 8. Explicitly out of scope (for v0.5)

These are good ideas. They are not for now.

- EPUB / book-native support → v0.7
- Multimodal (figures, tables, equations) → v0.8
- Hosted SaaS / web app → only after library traction proven
- Cross-document disagreement detection → v0.7
- Visual PDF bbox-level highlighting → v0.6 (maybe week 15)
- Custom-trained models → never
- Agent framework / tool use → never (we are not LangChain)
- Connectors (Slack, Notion, GDrive) → never (we are not Onyx)
- Audio overviews → never (we are not NotebookLM)

If a feature request doesn't strengthen the 5 core differentiators in §2, push back.

---

## 9. Risks and mitigations

| Risk | Mitigation |
|---|---|
| Constrained decoding doesn't work cleanly with closed APIs | Post-hoc attribution mode is the fallback (built in week 9 anyway) |
| Eval datasets lack span-level ground truth | Hand-annotate a 100–200 example test set in week 5 |
| Phase 3 takes 2 weeks longer than planned | Cut a SOTA module in week 15 |
| Motivation drops around week 10 | Public blog posts at each phase create external pressure |
| Competitor ships mid-build | Eval harness + integration breadth is the moat. Keep shipping. |
| LLM API costs run away during eval | Cache aggressively (Anthropic prompt caching, local NLI verifiers, eval on subsets in CI) |

---

## 10. Conventions

### Code
- Python 3.11+
- `ruff` for lint and format (replaces black, isort, flake8)
- `mypy --strict` on `src/verifiable_rag/`
- `pytest` with `pytest-asyncio`; smoke tests marked `@pytest.mark.smoke` run on every commit
- Public APIs: type-hinted dataclasses or pydantic models, never plain dicts
- All interfaces are `Protocol` or `ABC` so users can swap implementations

### Repo layout
```
src/verifiable_rag/
    models/       # Document, Sentence, Span, Answer, etc.
    parsers/
    chunkers/
    embedders/
    indexers/
    rerankers/
    generators/
    verifiers/
    pipeline.py
    eval/
        metrics.py
        runners.py
        datasets/
configs/          # YAML pipeline configs
examples/         # Runnable demos
benchmarks/       # Eval results, BENCHMARKS.md
docs/             # mkdocs site
tests/
```

### Commits and PRs
- Conventional commits: `feat:`, `fix:`, `docs:`, `bench:`, `refactor:`
- Every PR that touches `src/` must include or update tests
- Every PR that affects retrieval, generation, or verification must include eval-on-PR results in the description (CI does this automatically; just verify they're there)

### Versioning
- Semver. v0.x is unstable and we WILL break APIs to keep them clean.
- Pin versions of NLI models, embedders, and rerankers in configs — silent model updates have wrecked too many RAG benchmarks.

---

## 11. How to help on this project (for AI assistants)

### When asked to write code
- Read the relevant interface in `src/verifiable_rag/<layer>/__init__.py` first
- Preserve spans through every transformation. If your code breaks span tracking, it's wrong.
- Add a test in `tests/<layer>/` that round-trips a span through your change
- If the change touches retrieval, generation, or verification, run the eval harness locally and report numbers in your output

### When asked for design decisions
- Default to the stack in §5. Don't suggest LangChain chains or LlamaIndex's high-level abstractions for the core pipeline.
- If a request would compromise §6 (Hard rules), flag it explicitly and propose an alternative.
- If a request is in §8 (Out of scope), say so and ask if scope should change rather than silently building it.

### When asked to "improve" something
- Ask: which of the 5 differentiators in §2 does this strengthen? If none, push back.
- Ask: do we have a benchmark for this? If not, write the benchmark first.
- Don't tune hyperparameters by intuition. Numbers, not vibes.

### When asked about competitors
- The competitive landscape is in §3. Use it.
- We are NOT trying to beat NotebookLM on UX or Onyx on connectors. We are trying to be the most rigorous citation+verification library.

---

## 12. Open questions (revisit periodically)

- Do we expose `faithfulness_confidence` as a single number or as components (retrieval / generation / NLI)? Probably both — single number for end users, components for power users.
- How to surface "the model wanted to say X but couldn't verify it" without leaking unverified claims? Open design question for week 12.
- ColBERTv2 vs. cross-encoder reranker as default — depends on Phase 5 eval numbers.
- License: MIT (max adoption) vs. Apache 2.0 (patent grant) — leaning MIT but decide before public launch.
- Project name: `verifiable-rag` is a placeholder. Better names accepted.

---

## 13. References

Key papers and resources to cite/link in docs and blog posts:

- ReClaim: "Ground Every Sentence" — https://arxiv.org/abs/2407.01796
- SAFE: in-generation attribution — https://arxiv.org/abs/2505.12621
- LAQuer: localized attribution queries — ACL 2025
- HALT-RAG: dual-NLI ensemble — https://arxiv.org/html/2509.07475v1
- PaperQA2 — https://github.com/Future-House/paper-qa
- Contextual Retrieval (Anthropic) — https://www.anthropic.com/news/contextual-retrieval
- Late Chunking (Jina) — https://github.com/jina-ai/late-chunking
- HHEM-2.1-open — https://huggingface.co/vectara/hallucination_evaluation_model
- MiniCheck — https://huggingface.co/bespokelabs/Bespoke-MiniCheck-7B
- LitQA2 benchmark — FutureHouse
- RAGTruth — hallucination annotations
- FaithBench, HaluBench — faithfulness eval

---

*Last updated: April 2026. This file is the source of truth for project context. Update it when major decisions change.*
