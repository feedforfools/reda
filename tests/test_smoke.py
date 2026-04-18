"""Smoke tests: confirm all module stubs import cleanly."""

import importlib


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


def test_all_modules_importable() -> None:
    """Each module stub must import without raising any exception."""
    for name in MODULES:
        mod = importlib.import_module(name)
        assert mod is not None, f"Failed to import {name}"
