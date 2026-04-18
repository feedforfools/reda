"""Top-level pipeline orchestrator and CLI entry point."""

from __future__ import annotations

import logging
import sys
from typing import Literal

from models import RedactionResult

logger = logging.getLogger(__name__)


def process(
    text: str,
    use_ner: bool = True,
    use_gliner: bool = False,
    strategy: Literal["blanket", "pseudonym"] = "blanket",
) -> RedactionResult:
    """Run the full redaction pipeline on *text*.

    Args:
        text: The input document text.
        use_ner: Whether to run the NER layer.
        use_gliner: Whether to run the optional GLiNER layer.
        strategy: Redaction strategy — ``"blanket"`` replaces every entity with
            ``[OSCURATO]``; ``"pseudonym"`` uses typed indexed labels.

    Returns:
        A :class:`~models.RedactionResult` containing the redacted text and
        the list of detected entities.
    """
    raise NotImplementedError


if __name__ == "__main__":
    raise NotImplementedError("CLI entry point not yet implemented")
