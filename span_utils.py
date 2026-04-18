"""Span merging, deduplication, and overlap resolution utilities."""

import logging

from models import Span

logger = logging.getLogger(__name__)


def spans_overlap(a: Span, b: Span) -> bool:
    """Return True if spans *a* and *b* overlap.

    Args:
        a: First span.
        b: Second span.

    Returns:
        True if the spans share at least one character position.
    """
    raise NotImplementedError


def merge_spans(spans: list[Span]) -> list[Span]:
    """Merge spans from multiple sources into a deduplicated, non-overlapping list.

    Overlap resolution: prefer the longer span. On equal length, prefer ``"regex"``
    over ``"ner"`` over ``"gliner"``.

    Args:
        spans: Raw spans from any combination of layers.

    Returns:
        Deduplicated, non-overlapping spans sorted by start position.
    """
    raise NotImplementedError
