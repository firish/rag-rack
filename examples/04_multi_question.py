"""04 — multi-question pattern: ingest once, ask many.

For production / interactive use you want to pay the ingest cost
once and ask many questions over the same corpus. The top-level
``verifiable_rag.ask()`` is for one-shot use; for repeated queries,
build a Pipeline directly.

Requires
--------
- ANTHROPIC_API_KEY (generator)

Run
---
    python examples/04_multi_question.py
"""

from __future__ import annotations

from verifiable_rag import local_verified
from verifiable_rag.demo import sample_paper_path


QUESTIONS = [
    "Who discovered penicillin and when?",
    "What is the mechanism of action of penicillin?",
    "How does bacterial resistance to penicillin develop?",
    "What modern antibiotics are derived from penicillin?",
]


def main() -> None:
    print("Building pipeline (HHEM downloads on first run, ~600MB)...")
    pipeline = local_verified()

    print("Ingesting bundled sample PDF...")
    pipeline.ingest(sample_paper_path())

    for q in QUESTIONS:
        print()
        print("=" * 60)
        print(f"Q: {q}")
        answer = pipeline.ask(q)
        print(f"A: {answer.text}")
        print(
            f"   faithfulness={answer.faithfulness_score:.3f}, "
            f"unsupported={len(answer.unsupported_sentences)}/{len(answer.sentences)}, "
            f"refused={answer.was_refused}"
        )


if __name__ == "__main__":
    main()
