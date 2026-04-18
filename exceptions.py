"""Custom exception hierarchy for the reda project.

All exceptions inherit from :class:`RedaError` so callers can catch the entire
family with a single ``except RedaError`` clause.
"""

import logging

logger = logging.getLogger(__name__)


class RedaError(Exception):
    """Base exception for all reda errors."""


class RegexLayerError(RedaError):
    """Raised when the regex detection layer encounters an unrecoverable error."""


class NERLayerError(RedaError):
    """Raised when the NER model layer encounters an unrecoverable error."""


class GLiNERLayerError(RedaError):
    """Raised when the GLiNER layer encounters an unrecoverable error."""


class SpanUtilsError(RedaError):
    """Raised when span merging or deduplication fails."""


class RedactionError(RedaError):
    """Raised when the redaction step cannot be applied to the given text/spans."""


class PipelineError(RedaError):
    """Raised when the top-level pipeline orchestration fails."""
