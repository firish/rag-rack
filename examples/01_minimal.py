"""01 — minimal quickstart with verifiable_rag.ask().

The simplest possible usage: one PDF, one question, one print.

Requires
--------
- ANTHROPIC_API_KEY (the default generator is Haiku 4.5)

Run
---
    python examples/01_minimal.py
    python examples/01_minimal.py /path/to/your.pdf "Your question"
"""

from __future__ import annotations

import sys

import verifiable_rag
from verifiable_rag.demo import sample_paper_path


def main() -> None:
    pdf = sys.argv[1] if len(sys.argv) > 1 else str(sample_paper_path())
    question = (
        sys.argv[2]
        if len(sys.argv) > 2
        else "Who discovered penicillin and when?"
    )

    print(f"Question: {question}\nDocument: {pdf}\n")
    answer = verifiable_rag.ask(question, docs=pdf, preset="local_minimal")
    print("Answer:")
    print(answer.text)


if __name__ == "__main__":
    main()
