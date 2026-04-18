"""HuggingFace NER pipeline wrapper for DeepMount00/Italian_NER_XXL_v2."""

import logging

from models import Span

logger = logging.getLogger(__name__)


def detect(text: str) -> list[Span]:
    """Run the Italian NER model against *text* and return sorted spans.

    Args:
        text: The input document text.

    Returns:
        A list of :class:`Span` objects sorted by start position.
    """
    raise NotImplementedError
