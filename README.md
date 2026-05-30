# verifiable-rag

> Document-grounded Q&A with sentence-level citations, NLI verification, and calibrated refusal.

**Status:** pre-alpha · v0.5 launch sprint · interfaces are still subject to change

**📚 [Full documentation at firish.github.io/rag-rack](https://firish.github.io/rag-rack/)** — quickstart, concept guides, how-to recipes, API reference, benchmark reports.

---

## What this is

A Python library for building RAG pipelines that:

1. Produce **sentence-level citations** — every generated sentence traces back to exact source spans `(doc_id, page, char_start, char_end)`.
2. **Verify every claim** via NLI against its cited span before returning it.
3. **Refuse when uncertain** — calibrated abstention with a user-tunable strictness slider, not a "say I don't know" prompt.
4. Are **fully auditable** — inspect retrieval scores, reranker decisions, per-claim NLI results, and a self-contained HTML report per query.

**One benchmark result that drives the design:** on RAGTruth (the canonical 2,700-example RAG hallucination benchmark), a dual NLI ensemble of two small open-source models (HHEM-2.1-open + MiniCheck-Flan-T5-Large) matches Claude Sonnet 4.6 as a judge — **AUROC 0.844 vs 0.846 — at ~250× lower per-call cost.** Full result in [benchmarks/PUBLISHED_ragtruth.md](benchmarks/PUBLISHED_ragtruth.md).

## Quickstart

The bundled demo document ships with the package. No setup required beyond an LLM API key:

```python
import verifiable_rag
from verifiable_rag.demo import sample_paper_path

answer = verifiable_rag.ask(
    "What is the mechanism of action of penicillin?",
    docs=sample_paper_path(),
)
print(answer.text)
```

```bash
export ANTHROPIC_API_KEY=...
python -c "import verifiable_rag; from verifiable_rag.demo import sample_paper_path; \
           print(verifiable_rag.ask('Who discovered penicillin?', docs=sample_paper_path()).text)"
```

For an actual production setup, point `docs=` at your own PDFs and pick a preset:

```python
import verifiable_rag

answer = verifiable_rag.ask(
    "What did the authors find?",
    docs=["paper1.pdf", "paper2.pdf"],
    preset="hybrid_balanced",                  # RECOMMENDED — Cohere + Dual NLI + Haiku
    output_html="audit.html",                   # optional — write the HTML audit report
)
print(answer.text)

# Programmatic access to the audit trail:
for sentence in answer.unsupported_sentences:  # sentences the verifier flagged
    print(f"⚠ unsupported: {sentence.text}")

# Or emit a structured audit dump for logging / metrics:
metrics_client.emit(answer.audit_trail())
```

See [examples/](examples/) for runnable demos covering the headline UX patterns. The [full quickstart](https://firish.github.io/rag-rack/getting-started/quickstart/) walks through each step in detail.

## Presets

Five named presets cover most use cases. Switch via `preset="..."` or call the factories directly:

| Preset | Components | Required keys | When to use |
|---|---|---|---|
| `local_minimal` | BGE + PyMuPDF + Haiku, no verifier | `ANTHROPIC_API_KEY` | Hobbyist / quickest start |
| `local_verified` | + BGE rerank + HHEM NLI | `ANTHROPIC_API_KEY` | Local with verification |
| **`hybrid_balanced`** | **Docling + Cohere + Dual NLI + constrained Haiku** | `ANTHROPIC_API_KEY` + `COHERE_API_KEY` | **Default — the published baseline** |
| `hybrid_strict` | Same as balanced, refuse below faithfulness 0.7 | same | Higher-trust use cases |
| `hybrid_paranoid` | Sonnet generator, refuse below faithfulness 0.9 | same | Compliance / high-trust |

For mix-and-match outside the presets, use `verifiable_rag.build_pipeline(...)` or load a YAML config (see [examples/pipeline.yaml](examples/pipeline.yaml), `Pipeline.from_yaml()`, and the [YAML config guide](https://firish.github.io/rag-rack/how-to/yaml-config/)).

## Architecture

```
PDF/DOCX → Parser → Document model → Chunker → Indexer
                                                  ↓
Answer ← Abstention ← Verifier ← Generator ← Retriever + Reranker
```

Every step preserves character-level spans. Every generated sentence carries `(supporting_sentence_ids, confidence)` linked to exact source locations. Citation granularity is decoupled from chunk granularity by design.

## Audit trail

Every `Answer` exposes its full audit trail:

```python
answer = verifiable_rag.ask(question, docs=...)

answer.text                      # final answer string
answer.sentences                 # list of CitedSentence with supporting_sentence_ids
answer.verification_results      # per-sentence NLI checks
answer.retrieved_chunks          # the reranked passages the generator saw

# Convenience accessors:
answer.supported_sentences       # list[CitedSentence] (passed verification)
answer.unsupported_sentences     # list[CitedSentence] (verifier flagged)
answer.verification_for(idx)     # VerificationResult | None for a sentence index
answer.cited_sentence_ids        # frozenset of all source IDs cited
answer.min_nli_score             # worst-case sentence — the bottleneck
answer.audit_trail()             # JSON-serializable dict for logging / metrics

# Or render the full audit as a self-contained HTML page:
answer.to_html()                  # returns HTML string
# or pass output_html="report.html" to verifiable_rag.ask()
```

The HTML report includes the query, the answer with per-sentence verification color coding, the faithfulness components, per-sentence NLI scores, and every reranked passage with its retrieval score — citations are anchored links into the passage list.

## Installation

```bash
pip install verifiable-rag                          # core, no heavy deps
pip install "verifiable-rag[docling,bge,lancedb]"   # parser + embedder + index
pip install "verifiable-rag[hhem,minicheck]"        # NLI verifiers (adds torch + transformers)
pip install "verifiable-rag[litellm]"               # LLM-judge verifier
pip install "verifiable-rag[yaml]"                  # YAML config loader
pip install "verifiable-rag[all]"                   # everything
```

### First-run model downloads

Verifier model weights are **not bundled** in the wheel — they're downloaded lazily from HuggingFace Hub on first use and cached forever in `~/.cache/huggingface/hub/`.

| Verifier | Model | Size |
|---|---|---|
| `HHEMVerifier` | `vectara/hallucination_evaluation_model` | ~600 MB |
| `MiniCheckVerifier` | `lytang/MiniCheck-Flan-T5-Large` | ~770 MB |
| `LLMJudgeVerifier` | (hosted API, no local model) | 0 |

## Published benchmark results

| Benchmark | Headline | Report | Blog post |
|---|---|---|---|
| **ALCE** (Princeton citation quality) | Constrained decoding beats prompted by +4–7 F1 under dual-LLM-judge cross-validation | [report](benchmarks/PUBLISHED_alce.md) | [post](blog/02_constrained_citations.md) |
| **RAGTruth** (hallucination detection) | Dual NLI ensemble = Sonnet judge at 1/250× the cost (AUROC 0.844 vs 0.846) | [report](benchmarks/PUBLISHED_ragtruth.md) | [post](blog/03_verified_rag.md) |
| **LitQA2** (biomedical scientific Q&A) | Constrained decoding lifts MC; contextual retrieval is a null result on saturated retrieval | [report](benchmarks/PUBLISHED_litqa2.md) | [post](blog/04_litqa2_ablation.md) |

## Roadmap

| Phase | Milestone | Status |
|---|---|---|
| 0–1 | Repo skeleton, data model, baseline pipeline | ✅ done |
| 2 | Eval harness + BENCHMARKS.md | ✅ done |
| 3 | Sentence-level citations (prompted / constrained / SAFE) | ✅ done |
| 4 | Faithfulness verification + calibrated refusal (v0.4) | ✅ done |
| 5 | Hardening, mkdocs docs, Gradio demo on HF Spaces (v0.5) | in progress |
| 6 | Launch — PyPI release + Show HN | pending |

## Contributing

See [CLAUDE.md](CLAUDE.md) for architecture decisions, hard rules, and contribution conventions. Methodology critiques on the published benchmarks are especially welcome — eval rigor is the whole moat, and the only way to find the holes is to invite people to look for them.

## License

MIT
