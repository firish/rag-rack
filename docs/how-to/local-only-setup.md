# Local-only setup (no API keys)

A configuration that runs entirely on your machine — no API keys, no outbound network calls after the initial model downloads. Useful for air-gapped environments, regulated industries, and "I just want to evaluate the library without setting up cloud accounts" testing.

## What's local-only

| Component | Local-only choice | Notes |
|---|---|---|
| Parser | `PyMuPDFParser` | Fast, text-only. Use `DoclingParser` if you have GPU / are OK with OCR slowness. |
| Chunker | `ParentChildChunker` | Pure-Python, always local. |
| Embedder | `SentenceTransformerEmbedder` (BGE-small) | ~140 MB model, runs on CPU/MPS/CUDA. |
| Indexer | `LanceDBIndex + BM25Index` | Both file-backed, no server. |
| Reranker | `BGERerankerV2` | ~568 MB model, optional. Skip with `reranker=None` for the leanest path. |
| Generator | `PromptedCitedGenerator` + Ollama | Local LLM via Ollama. |
| Verifier | `HHEMVerifier` (single) or `DualNLIVerifier` (HHEM + MiniCheck) | ~600 MB and ~770 MB models. |

## Step 1: Install with local extras only

```bash
pip install "verifiable-rag[pymupdf,bge,lancedb,bm25,litellm,hhem,minicheck]"
```

This skips the hosted-API SDKs (Cohere, Voyage) — about 50 MB lighter.

## Step 2: Start Ollama

[Ollama](https://ollama.com/) is the easiest way to serve a local LLM with an OpenAI-compatible API. Install it for your platform, then:

```bash
ollama pull llama3.1
ollama serve
```

By default Ollama listens on `http://localhost:11434`. LiteLLM has built-in support for it.

## Step 3: Build the pipeline

```python
from verifiable_rag import Pipeline
from verifiable_rag.chunkers import ParentChildChunker
from verifiable_rag.embedders import SentenceTransformerEmbedder
from verifiable_rag.generators import PromptedCitedGenerator
from verifiable_rag.indexers import BM25Index, HybridIndex, LanceDBIndex
from verifiable_rag.parsers import PyMuPDFParser
from verifiable_rag.rerankers import BGERerankerV2
from verifiable_rag.verifiers import DualNLIVerifier, HHEMVerifier, MiniCheckVerifier

pipeline = Pipeline(
    parser=PyMuPDFParser(),
    chunker=ParentChildChunker(max_child_tokens=400, min_child_tokens=100),
    embedder=SentenceTransformerEmbedder(model_name="BAAI/bge-small-en-v1.5"),
    indexer=HybridIndex(
        dense=LanceDBIndex(uri="./my_index"),
        sparse=BM25Index(),
    ),
    reranker=BGERerankerV2(),
    generator=PromptedCitedGenerator(
        model="ollama/llama3.1",
        api_base="http://localhost:11434",
    ),
    verifier=DualNLIVerifier(HHEMVerifier(), MiniCheckVerifier()),
    strictness="balanced",
)

pipeline.ingest("paper.pdf")
answer = pipeline.ask("What did the authors find?")
print(answer.text)
```

## Step 4: First-run model downloads

On the first call, three models download from HuggingFace Hub to `~/.cache/huggingface/hub/`:

| Model | Size | Used by |
|---|---|---|
| `BAAI/bge-small-en-v1.5` | ~140 MB | Embedder |
| `BAAI/bge-reranker-v2-m3` | ~568 MB | Reranker |
| `vectara/hallucination_evaluation_model` | ~600 MB | HHEMVerifier |
| `lytang/MiniCheck-Flan-T5-Large` | ~770 MB | MiniCheckVerifier |

Total: ~2 GB. Cached forever after the first download. The library uses standard `transformers` / `sentence-transformers` machinery — no library-specific download path.

For air-gapped setups, pre-download these on a connected machine and copy the cache directory to the air-gapped machine.

## Pre-downloading models for air-gapped install

```bash
# On a connected machine:
python -c "
from sentence_transformers import SentenceTransformer
SentenceTransformer('BAAI/bge-small-en-v1.5')
from FlagEmbedding import FlagReranker
FlagReranker('BAAI/bge-reranker-v2-m3')
from transformers import AutoModelForSequenceClassification, AutoModelForSeq2SeqLM, AutoTokenizer
AutoModelForSequenceClassification.from_pretrained('vectara/hallucination_evaluation_model', trust_remote_code=True)
AutoTokenizer.from_pretrained('lytang/MiniCheck-Flan-T5-Large')
AutoModelForSeq2SeqLM.from_pretrained('lytang/MiniCheck-Flan-T5-Large')
"
# Then tar the HF cache and copy:
tar -czf hf_cache.tar.gz ~/.cache/huggingface/
# Transfer hf_cache.tar.gz to the air-gapped machine and extract to ~/.cache/huggingface/
```

## Hardware sizing

Approximate VRAM / RAM requirements for the local-only stack:

| Component | CPU OK? | GPU recommended? | VRAM/RAM |
|---|---|---|---|
| BGE-small embedder | Yes | Optional | ~500 MB CPU, ~1 GB GPU |
| BGE reranker v2 | Yes | Yes (10x faster) | ~2 GB CPU, ~2 GB GPU |
| HHEM verifier | Yes | Yes | ~2 GB CPU, ~2.5 GB GPU |
| MiniCheck verifier | Yes | Yes | ~2.5 GB CPU, ~3 GB GPU |
| Llama 3.1 8B (via Ollama) | Yes | Strongly recommended | ~5 GB CPU, ~5 GB GPU |

A 16 GB consumer GPU runs the full stack comfortably. A 32 GB Apple Silicon Mac handles it on CPU/MPS.

## What you give up

- **Generator quality.** Llama 3.1 8B via Ollama is meaningfully worse than Claude Haiku on citation correctness. Expect ~5-10pp F1 drop on benchmarks like ALCE.
- **Constrained-decoding citations.** `ConstrainedCitedGenerator` requires structured-output support; Ollama doesn't have it (yet). Use `PromptedCitedGenerator` instead.
- **Cohere embed/rerank quality.** BGE-small is ~5-10pp worse on retrieval benchmarks compared to Cohere embed-v3. Add the reranker to claw most of that back.

## Verification (smoke test)

Quick sanity check that the local-only flow works end-to-end:

```python
from verifiable_rag.demo import sample_paper_path

answer = pipeline.ask("What is the mechanism of action of penicillin?")
print(answer.text)
print(f"\nfaithfulness={answer.faithfulness_score:.3f}, refused={answer.was_refused}")
```

If you see a coherent answer with non-zero faithfulness — you're done. If you see an empty answer or a refusal, drop strictness to `loose` to debug:

```python
pipeline.strictness = "loose"
```

Then look at `answer.verification_results` to see what the verifier flagged. See [Render audit HTML](render-audit-html.md) for the diagnostic shortcuts.
