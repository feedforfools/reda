"""Pydantic v2 data models shared across all layers."""

import logging
from typing import Literal

from pydantic import BaseModel, Field, model_validator

logger = logging.getLogger(__name__)


class Span(BaseModel):
    """A detected PII span within a document."""

    start: int = Field(ge=0)
    end: int = Field(ge=1)
    text: str = Field(min_length=1)
    label: str = Field(min_length=1)
    source: Literal["regex", "ner", "gliner"]
    confidence: float | None = Field(default=None, ge=0.0, le=1.0)

    @model_validator(mode="after")
    def end_after_start(self) -> "Span":
        if self.end <= self.start:
            raise ValueError(f"end ({self.end}) must be greater than start ({self.start})")
        return self


class RedactionResult(BaseModel):
    """The result of running the full redaction pipeline on a document."""

    original_text: str = Field(min_length=1)
    redacted_text: str
    entities: list[Span] = Field(default_factory=list)
