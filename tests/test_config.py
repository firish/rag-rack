"""Config loader + registry tests."""

from __future__ import annotations

import sys
from pathlib import Path
from unittest.mock import MagicMock

import pytest

from verifiable_rag.config import (
    _instantiate,
    load_pipeline_from_yaml,
    register,
    registered_types,
)


# --------------------------------------------------------------------------- #
# Registry discoverability
# --------------------------------------------------------------------------- #


@pytest.mark.smoke
def test_registered_types_lists_all_components() -> None:
    types = registered_types()
    assert "parser" in types
    assert "embedder" in types
    assert "generator" in types
    assert "verifier" in types
    # At least one type registered per component (built-ins)
    assert types["parser"]
    assert types["embedder"]


@pytest.mark.smoke
def test_registered_types_includes_known_builtins() -> None:
    types = registered_types()
    assert "docling" in types["parser"]
    assert "pymupdf" in types["parser"]
    assert "bge" in types["embedder"]
    assert "cohere" in types["embedder"]
    assert "prompted" in types["generator"]
    assert "constrained" in types["generator"]
    assert "safe" in types["generator"]
    assert "dual_nli" in types["verifier"]
    assert "hhem" in types["scorer"]
    assert "minicheck" in types["scorer"]


@pytest.mark.smoke
def test_register_adds_factory() -> None:
    """A new factory registered via the decorator shows up in the registry."""

    @register("parser", "_test_dummy_parser_")
    def _factory(**_kw: object) -> str:
        return "dummy"

    assert "_test_dummy_parser_" in registered_types()["parser"]


@pytest.mark.smoke
def test_register_rejects_unknown_component() -> None:
    with pytest.raises(ValueError, match="Unknown component"):
        register("badcomponent", "x")


@pytest.mark.smoke
def test_instantiate_unknown_type_raises_helpful_error() -> None:
    with pytest.raises(ValueError, match="Unknown parser type"):
        _instantiate("parser", "nope_does_not_exist", {})


# --------------------------------------------------------------------------- #
# YAML loading — uses mocks for heavy components so no models download
# --------------------------------------------------------------------------- #


@pytest.fixture
def minimal_yaml(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Path:
    """Write a minimal-but-complete YAML config to disk + mock the heavy
    factories so we don't load real models."""
    yaml_content = """
parser:
  type: pymupdf

chunker:
  type: parent_child
  config:
    max_child_tokens: 200
    min_child_tokens: 0

embedder:
  type: bge

indexer:
  dense:
    type: lancedb
    uri: /tmp/test_idx
  sparse:
    type: bm25

reranker:
  type: none

generator:
  type: prompted
  config:
    model: anthropic/claude-haiku-4-5

verifier:
  type: none

pipeline:
  strictness: balanced
  top_k_retrieve: 20
  top_k_rerank: 5
"""
    path = tmp_path / "pipeline.yaml"
    path.write_text(yaml_content)

    # Patch heavy factories to return MagicMocks. We're testing the loader's
    # routing logic, not the components' internals.
    import verifiable_rag.config as cfg

    monkeypatch.setitem(cfg._REGISTRY["parser"], "pymupdf", lambda **_: MagicMock(name="parser"))
    monkeypatch.setitem(cfg._REGISTRY["embedder"], "bge", lambda **_: MagicMock(name="embedder"))
    monkeypatch.setitem(cfg._REGISTRY["dense_indexer"], "lancedb", lambda **_: MagicMock(name="dense"))
    monkeypatch.setitem(cfg._REGISTRY["sparse_indexer"], "bm25", lambda **_: MagicMock(name="sparse"))
    monkeypatch.setitem(cfg._REGISTRY["generator"], "prompted", lambda **_: MagicMock(name="generator"))
    return path


@pytest.mark.smoke
def test_load_pipeline_from_yaml_builds_pipeline(minimal_yaml: Path) -> None:
    from verifiable_rag.pipeline import Pipeline

    pipeline = load_pipeline_from_yaml(minimal_yaml)
    assert isinstance(pipeline, Pipeline)
    assert pipeline.strictness == "balanced"
    assert pipeline.top_k_retrieve == 20
    assert pipeline.top_k_rerank == 5


@pytest.mark.smoke
def test_pipeline_from_yaml_classmethod_works(minimal_yaml: Path) -> None:
    from verifiable_rag import Pipeline

    pipeline = Pipeline.from_yaml(minimal_yaml)
    assert isinstance(pipeline, Pipeline)


@pytest.mark.smoke
def test_yaml_optional_reranker_none_yields_no_reranker(minimal_yaml: Path) -> None:
    pipeline = load_pipeline_from_yaml(minimal_yaml)
    assert pipeline.reranker is None


@pytest.mark.smoke
def test_yaml_optional_verifier_none_yields_no_verifier(minimal_yaml: Path) -> None:
    pipeline = load_pipeline_from_yaml(minimal_yaml)
    assert pipeline.verifier is None


@pytest.mark.smoke
def test_yaml_passes_chunker_config_through(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    """Config values for the chunker reach the factory."""
    captured: dict[str, object] = {}

    import verifiable_rag.config as cfg

    def _chunker_factory(**kw: object) -> object:
        captured.update(kw)
        return MagicMock()

    monkeypatch.setitem(cfg._REGISTRY["chunker"], "parent_child", _chunker_factory)
    monkeypatch.setitem(cfg._REGISTRY["parser"], "pymupdf", lambda **_: MagicMock())
    monkeypatch.setitem(cfg._REGISTRY["embedder"], "bge", lambda **_: MagicMock())
    monkeypatch.setitem(cfg._REGISTRY["dense_indexer"], "lancedb", lambda **_: MagicMock())
    monkeypatch.setitem(cfg._REGISTRY["sparse_indexer"], "bm25", lambda **_: MagicMock())
    monkeypatch.setitem(cfg._REGISTRY["generator"], "prompted", lambda **_: MagicMock())

    yaml_path = tmp_path / "p.yaml"
    yaml_path.write_text(
        """
parser:
  type: pymupdf
chunker:
  type: parent_child
  config:
    max_child_tokens: 777
    min_child_tokens: 50
embedder:
  type: bge
indexer:
  dense:
    type: lancedb
  sparse:
    type: bm25
generator:
  type: prompted
"""
    )
    load_pipeline_from_yaml(yaml_path)
    assert captured.get("max_child_tokens") == 777
    assert captured.get("min_child_tokens") == 50


@pytest.mark.smoke
def test_yaml_unknown_type_raises_helpful_error(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    """Bad component type in YAML gives a clear error pointing at the type name."""
    import verifiable_rag.config as cfg

    monkeypatch.setitem(cfg._REGISTRY["embedder"], "bge", lambda **_: MagicMock())
    monkeypatch.setitem(cfg._REGISTRY["dense_indexer"], "lancedb", lambda **_: MagicMock())
    monkeypatch.setitem(cfg._REGISTRY["sparse_indexer"], "bm25", lambda **_: MagicMock())
    monkeypatch.setitem(cfg._REGISTRY["generator"], "prompted", lambda **_: MagicMock())

    yaml_path = tmp_path / "bad.yaml"
    yaml_path.write_text(
        """
parser:
  type: NOPE_NOT_A_PARSER
chunker:
  type: parent_child
embedder:
  type: bge
indexer:
  dense:
    type: lancedb
  sparse:
    type: bm25
generator:
  type: prompted
"""
    )
    with pytest.raises(ValueError, match="Unknown parser type 'NOPE_NOT_A_PARSER'"):
        load_pipeline_from_yaml(yaml_path)
