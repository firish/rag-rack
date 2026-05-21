# verifiable-rag

> Document-grounded Q&A with sentence-level citations and faithfulness verification.

**Status:** Phase 0 — foundations (pre-alpha, interfaces not yet stable)

---

## What this is

A Python library for building RAG pipelines that:

1. Produce **sentence-level citations** — every generated sentence traces back to exact source spans `(doc_id, page, char_start, char_end)`
2. **Verify every claim** via NLI against its cited span before returning it
3. **Refuse when uncertain** — calibrated abstention with a user-tunable strictness slider, not a "say I don't know" prompt
4. Are **fully auditable** — inspect retrieval scores, reranker decisions, and per-claim NLI results

## Why

Every shipping "chat with your documents" product (NotebookLM, ChatPDF, Humata, Adobe Acrobat AI) stops at chunk-level citations and prompt-conditioned grounding. The 2024–2026 research literature — ReClaim, SAFE, HALT-RAG — has solved sentence-span attribution and post-hoc faithfulness verification. None of it has shipped in a usable library.

## Architecture

```
PDF/DOCX → Parser → Document model → Chunker → Indexer
                                                  ↓
Answer ← Abstention ← Verifier ← Generator ← Retriever + Reranker
```

Every step preserves character-level spans. Every generated sentence carries `(supporting_sentence_ids, confidence)` linked to exact source locations. See [CLAUDE.md](CLAUDE.md) for the full architecture.

## Quickstart

```python
# Coming in Phase 1 (week 2–4)
from verifiable_rag import Pipeline
from verifiable_rag.parsers import DoclingParser
from verifiable_rag.chunkers import RecursiveChunker
from verifiable_rag.generators import CitedGenerator
from verifiable_rag.verifiers import HHEMVerifier

pipeline = Pipeline(
    parser=DoclingParser(),
    chunker=RecursiveChunker(chunk_size=512),
    generator=CitedGenerator(mode="prompted"),
    verifier=HHEMVerifier(strictness="balanced"),
)

pipeline.ingest("paper.pdf")
answer = pipeline.ask("What did the authors find?")
# answer.sentences  -> [(text, [sent_ids], confidence), ...]
# answer.faithfulness_score  -> 0.91
# answer.unsupported_claims  -> []
```

## Installation

```bash
pip install verifiable-rag                          # core (no heavy deps)
pip install "verifiable-rag[docling,bge,lancedb]"   # with parser + embedder + index
pip install "verifiable-rag[hhem,minicheck]"        # NLI verifiers (adds torch + transformers)
pip install "verifiable-rag[litellm]"               # LLM-judge verifier
pip install "verifiable-rag[all]"                   # everything
```

### First-run model downloads

Verifier model weights are **not bundled** in the wheel — they're downloaded lazily from HuggingFace Hub on first use, then cached in `~/.cache/huggingface/hub/`. Expect a one-time download per verifier:

| Verifier | Model | Size |
|---|---|---|
| `HHEMVerifier` | `vectara/hallucination_evaluation_model` | ~600 MB |
| `MiniCheckVerifier` | `lytang/MiniCheck-Flan-T5-Large` | ~770 MB |
| `LLMJudgeVerifier` | (none — calls a hosted API) | 0 |

After the first call the model is cached forever. Standard `transformers` progress bar is shown during download.

## Roadmap

| Phase | Weeks | Milestone |
|-------|-------|-----------|
| 0 | 1 | Repo skeleton, data model, interfaces, benchmark loaders |
| 1 | 2–4 | Baseline pipeline, public repo |
| 2 | 5–6 | Eval harness, `BENCHMARKS.md` |
| 3 | 7–9 | Sentence-level citations in 3 modes |
| 4 | 10–12 | Faithfulness verification + calibrated refusal (v0.4) |
| 5 | 13–15 | Hardening, Gradio demo, SOTA modules (v0.5) |

## Contributing

See [CLAUDE.md](CLAUDE.md) for architecture decisions, hard rules, and contribution conventions.

## License

MIT
