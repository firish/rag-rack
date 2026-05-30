"""05 — load a Pipeline from YAML + discover available component types.

For customization beyond the named presets, describe your pipeline in
YAML and let ``Pipeline.from_yaml()`` wire it up. This example also
shows ``registered_types()`` — runtime introspection of every component
type the loader (and any registry-driven tool) understands.

Requires
--------
- ANTHROPIC_API_KEY (generator)
- COHERE_API_KEY (the bundled examples/pipeline.yaml uses Cohere)

Run
---
    python examples/05_yaml_config.py
"""

from __future__ import annotations

from pathlib import Path

from verifiable_rag import Pipeline
from verifiable_rag.config import registered_types
from verifiable_rag.demo import sample_paper_path


def main() -> None:
    # --- Discoverability: what types are available? ---------------------
    print("Component types known to the YAML loader:")
    for component, types in registered_types().items():
        print(f"  {component}: {types}")
    print()

    # --- Load a Pipeline from YAML --------------------------------------
    yaml_path = Path("examples/pipeline.yaml")
    print(f"Loading pipeline from {yaml_path}...")
    pipeline = Pipeline.from_yaml(yaml_path)

    print("Ingesting sample doc...")
    pipeline.ingest(sample_paper_path())

    answer = pipeline.ask(
        "What classes of antibiotics share the beta-lactam ring?"
    )
    print()
    print("Answer:")
    print(answer.text)
    print(f"\nfaithfulness={answer.faithfulness_score:.3f} · "
          f"strictness={answer.strictness} · refused={answer.was_refused}")


if __name__ == "__main__":
    main()
