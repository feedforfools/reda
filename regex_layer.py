"""Regex-based detection of structured Italian PII."""

import logging

from models import Span

logger = logging.getLogger(__name__)


def detect(text: str) -> list[Span]:
    """Run all regex patterns against *text* and return sorted, non-overlapping spans.

    Args:
        text: The input document text.

    Returns:
        A list of :class:`Span` objects sorted by start position.
    """
    raise NotImplementedError
