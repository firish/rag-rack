"""02 — generate the HTML audit report.

Same flow as 01, but writes a self-contained HTML page showing the
answer, per-sentence verification, faithfulness scores, and every
reranked passage the generator saw. Open it in any browser.

Requires
--------
- ANTHROPIC_API_KEY (generator)

The audit report uses the local NLI verifier (HHEM-2.1-open, ~600MB,
downloaded on first call), so per-sentence verification colors show
up. Use ``preset="local_minimal"`` to skip verification.

Run
---
    python examples/02_audit_html.py
    open /tmp/verifiable_rag_demo.html
"""

from __future__ import annotations

from pathlib import Path

import verifiable_rag
from verifiable_rag.demo import sample_paper_path


def main() -> None:
    output_html = Path("/tmp/verifiable_rag_demo.html")
    answer = verifiable_rag.ask(
        "What is the mechanism of action of penicillin?",
        docs=sample_paper_path(),
        preset="local_verified",  # includes HHEM verifier for the audit colors
        output_html=output_html,
        output_html_title="Penicillin demo — verifiable-rag",
    )
    print(f"Answer:\n{answer.text}\n")
    print(f"Audit report → {output_html}")
    print(f"Open with: open {output_html}")


if __name__ == "__main__":
    main()
