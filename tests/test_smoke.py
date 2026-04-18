"""Smoke tests: confirm all module stubs import cleanly."""

import importlib

import pytest

MODULES = [
    "models",
    "exceptions",
    "regex_layer",
    "ner_layer",
    "gliner_layer",
    "span_utils",
    "redact",
    "pipeline",
]


@pytest.mark.parametrize("module_name", MODULES)
def test_module_importable(module_name: str) -> None:
    """Each module stub must import without raising any exception."""
    mod = importlib.import_module(module_name)
    assert mod is not None
