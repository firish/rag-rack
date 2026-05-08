"""End-to-end demo: ingest a PDF, ask a question, print a cited answer.

Usage:
    # Default sample PDF + a sample question
    python examples/ask_pdf.py

    # Your own PDF + question
    python examples/ask_pdf.py path/to/file.pdf "What does the author claim about X?"

    # Pick a different LLM (any LiteLLM model string)
    VRAG_MODEL="groq/llama-3.3-70b-versatile" python examples/ask_pdf.py

The pipeline runs in *loose* strictness mode (no verifier yet — that's Phase 4).
You'll need:
  * docling, wtpsplit, sentence-transformers, lancedb, bm25s, litellm installed
  * an LLM API key in env, matching the model:
      - groq/...     -> GROQ_API_KEY      (free tier — get one at console.groq.com)
      - claude-...   -> ANTHROPIC_API_KEY
      - openai/...   -> OPENAI_API_KEY
      - gemini/...   -> GEMINI_API_KEY
    See https://docs.litellm.ai for the full provider list.
"""

from __future__ import annotations

import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from verifiable_rag.chunkers import ParentChildChunker
from verifiable_rag.embedders import SentenceTransformerEmbedder
from verifiable_rag.generators import PromptedCitedGenerator
from verifiable_rag.indexers import BM25Index, HybridIndex, LanceDBIndex
from verifiable_rag.parsers import CachingParser, DoclingParser
from verifiable_rag.pipeline import Pipeline

_DEFAULT_PDF = Path("tests/parsers/fixtures/sample.pdf")
_DEFAULT_QUESTION = "What is this document about? Summarize the main claims."
_DEFAULT_MODEL = os.environ.get("VRAG_MODEL", "groq/llama-3.3-70b-versatile")


def build_pipeline(model: str = _DEFAULT_MODEL) -> Pipeline:
    """Wire up the baseline pipeline.  No reranker, no verifier (Phase 4)."""
    return Pipeline(
        parser=CachingParser(DoclingParser()),
        chunker=ParentChildChunker(max_child_tokens=400),
        embedder=SentenceTransformerEmbedder(model_name="BAAI/bge-small-en-v1.5"),
        indexer=HybridIndex(
            dense=LanceDBIndex(uri=Path(".verifiable_rag_cache/indexes/demo_lance")),
            sparse=BM25Index(),
        ),
        generator=PromptedCitedGenerator(model=model),
        strictness="loose",
        top_k_retrieve=40,
        top_k_rerank=15,
    )


def main(pdf_path: Path, question: str) -> None:
    print(f"\nModel:     {_DEFAULT_MODEL}")
    print(f"Ingesting: {pdf_path}")
    print("-" * 70)

    pipeline = build_pipeline()
    document = pipeline.ingest(pdf_path)
    print(
        f"Indexed: {len(document.sentences)} sentences, "
        f"{len(document.paragraphs)} paragraphs, {document.num_pages} pages"
    )

    print(f"\nQuestion: {question}")
    print("-" * 70)

    answer = pipeline.ask(question)

    if answer.was_refused:
        print(f"\n[REFUSED] {answer.refusal_reason}")
        return

    if not answer.sentences:
        print("\n[EMPTY] Generator produced no answer.")
        return

    print("\nAnswer:")
    for i, sent in enumerate(answer.sentences, start=1):
        cites = ", ".join(sent.supporting_sentence_ids) or "(uncited)"
        print(f"  {i}. {sent.text}")
        print(f"     -> [{cites}]  conf={sent.confidence:.2f}")

    print("\nFaithfulness components:")
    print(f"  retrieval_score : {answer.faithfulness_components.retrieval_score:.3f}")
    print(f"  nli_score       : {answer.faithfulness_components.nli_score:.3f}")
    print(f"  combined        : {answer.faithfulness_score:.3f}")

    if answer.unsupported_claims:
        print(f"\nUnsupported claims ({len(answer.unsupported_claims)}):")
        for claim in answer.unsupported_claims:
            print(f"  - {claim}")

    print(f"\nRetrieved chunks used: {len(answer.retrieved_chunks)}")
    for rc in answer.retrieved_chunks[:3]:
        snippet = rc.chunk.text[:100].replace("\n", " ")
        print(f"  [{rc.chunk.chunk_id}] score={rc.score:.3f}  {snippet!r}...")


if __name__ == "__main__":
    if len(sys.argv) >= 3:
        main(Path(sys.argv[1]), sys.argv[2])
    elif len(sys.argv) == 2:
        main(Path(sys.argv[1]), _DEFAULT_QUESTION)
    else:
        if _DEFAULT_PDF.exists():
            main(_DEFAULT_PDF, _DEFAULT_QUESTION)
        else:
            print(
                "Usage:\n"
                "  python examples/ask_pdf.py <pdf_path> [question]\n"
                f"\nNo PDF given and {_DEFAULT_PDF} does not exist."
            )
            sys.exit(1)
