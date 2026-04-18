"""Pydantic v2 data models shared across all layers."""

import logging
from typing import Literal

from pydantic import BaseModel

logger = logging.getLogger(__name__)


class Span(BaseModel):
    """A detected PII span within a document."""

    start: int
    end: int
    text: str
    label: str
    source: Literal["regex", "ner", "gliner"]
    confidence: float | None = None


class RedactionResult(BaseModel):
    """The result of running the full redaction pipeline on a document."""

    original_text: str
    redacted_text: str
    entities: list[Span]
