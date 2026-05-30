"""03 — programmatic access to the audit trail.

Shows the Answer convenience properties you'd reach for when wrapping
verifiable-rag in a larger application: filter unsupported sentences,
collect cited source IDs, emit a structured audit record for logging
or metrics.

Requires
--------
- ANTHROPIC_API_KEY (generator)

Run
---
    python examples/03_audit_trail.py
"""

from __future__ import annotations

import json

import verifiable_rag
from verifiable_rag.demo import sample_paper_path


def main() -> None:
    answer = verifiable_rag.ask(
        "How does bacterial resistance to penicillin develop?",
        docs=sample_paper_path(),
        preset="local_verified",
    )

    print("=" * 60)
    print("Answer text:")
    print(answer.text)
    print()

    # Filter sentences by verification status
    print("=" * 60)
    print(f"Supported sentences: {len(answer.supported_sentences)}")
    for s in answer.supported_sentences:
        print(f"  ✓ {s.text}")

    print(f"\nUnsupported sentences: {len(answer.unsupported_sentences)}")
    for s in answer.unsupported_sentences:
        print(f"  ✗ {s.text}")

    # Look up the verification result for a specific sentence
    print()
    print("=" * 60)
    print("Per-sentence NLI scores:")
    for i, sent in enumerate(answer.sentences):
        vr = answer.verification_for(i)
        if vr is not None:
            mark = "✓" if vr.is_supported else "✗"
            print(f"  [{i}] {mark} nli={vr.nli_score:.3f}  {sent.text[:60]}...")

    # Source sentences cited
    print()
    print("=" * 60)
    print(f"Cited source sentence IDs ({len(answer.cited_sentence_ids)}):")
    for sid in sorted(answer.cited_sentence_ids):
        print(f"  - {sid}")

    # Structured audit dump — drop-in for JSON logging / metrics
    print()
    print("=" * 60)
    print("Structured audit_trail() — JSON-serializable:")
    print(json.dumps(answer.audit_trail(), indent=2))


if __name__ == "__main__":
    main()
