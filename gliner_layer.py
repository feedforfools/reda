"""Optional supplementary NER pass using knowledgator/gliner-pii-base-v1.0."""

import logging

from models import Span

logger = logging.getLogger(__name__)


def detect(text: str, labels: list[str] | None = None) -> list[Span]:
    """Run the GLiNER zero-shot PII model against *text*.

    Args:
        text: The input document text.
        labels: Entity type labels to detect. Defaults to a built-in set covering
            categories not well-represented in the Italian NER model.

    Returns:
        A list of :class:`Span` objects sorted by start position.
    """
    raise NotImplementedError
