"""Evaluation harness for verifiable-rag.

Metrics implemented here operate at span-level, not chunk-level, to match
the library's core thesis. Wrap RAGAS/DeepEval for chunk-level baselines.
"""
