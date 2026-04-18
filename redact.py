"""Applies a redaction strategy to text given a merged span list."""

import logging

from models import Span

logger = logging.getLogger(__name__)


def redact_blanket(text: str, spans: list[Span]) -> str:
    """Replace every span in *text* with ``[OSCURATO]``.

    Args:
        text: The original document text.
        spans: Non-overlapping spans sorted by start position.

    Returns:
        The redacted text.
    """
    raise NotImplementedError


def redact_pseudonym(text: str, spans: list[Span]) -> str:
    """Replace spans with typed, indexed labels (e.g. ``[PERSONA_1]``).

    The same original text value receives the same label within a document.

    Args:
        text: The original document text.
        spans: Non-overlapping spans sorted by start position.

    Returns:
        The redacted text with consistent pseudonyms.
    """
    raise NotImplementedError
