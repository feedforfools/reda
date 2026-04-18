"""Unit tests for models.py — Span and RedactionResult."""

import pytest
from pydantic import ValidationError

from models import RedactionResult, Span


# ---------------------------------------------------------------------------
# Span — valid construction
# ---------------------------------------------------------------------------


def test_span_valid_minimal() -> None:
    span = Span(start=0, end=5, text="Mario", label="PERSONA", source="regex")
    assert span.start == 0
    assert span.end == 5
    assert span.confidence is None


def test_span_valid_with_confidence() -> None:
    span = Span(start=10, end=20, text="RSSMRA80A01H501U", label="CODICE_FISCALE", source="ner", confidence=0.95)
    assert span.confidence == 0.95


def test_span_confidence_boundary_values() -> None:
    Span(start=0, end=1, text="x", label="L", source="regex", confidence=0.0)
    Span(start=0, end=1, text="x", label="L", source="regex", confidence=1.0)


# ---------------------------------------------------------------------------
# Span — invalid construction
# ---------------------------------------------------------------------------


def test_span_negative_start_raises() -> None:
    with pytest.raises(ValidationError):
        Span(start=-1, end=5, text="Mario", label="PERSONA", source="regex")


def test_span_end_zero_raises() -> None:
    with pytest.raises(ValidationError):
        Span(start=0, end=0, text="Mario", label="PERSONA", source="regex")


def test_span_end_equal_start_raises() -> None:
    with pytest.raises(ValidationError):
        Span(start=5, end=5, text="x", label="L", source="regex")


def test_span_end_before_start_raises() -> None:
    with pytest.raises(ValidationError):
        Span(start=10, end=5, text="x", label="L", source="regex")


def test_span_empty_text_raises() -> None:
    with pytest.raises(ValidationError):
        Span(start=0, end=1, text="", label="L", source="regex")


def test_span_empty_label_raises() -> None:
    with pytest.raises(ValidationError):
        Span(start=0, end=1, text="x", label="", source="regex")


def test_span_confidence_below_zero_raises() -> None:
    with pytest.raises(ValidationError):
        Span(start=0, end=1, text="x", label="L", source="ner", confidence=-0.1)


def test_span_confidence_above_one_raises() -> None:
    with pytest.raises(ValidationError):
        Span(start=0, end=1, text="x", label="L", source="ner", confidence=1.01)


def test_span_invalid_source_raises() -> None:
    with pytest.raises(ValidationError):
        Span(start=0, end=1, text="x", label="L", source="unknown")


# ---------------------------------------------------------------------------
# Span — serialization round-trip
# ---------------------------------------------------------------------------


def test_span_serialization_roundtrip() -> None:
    span = Span(start=3, end=9, text="Firenze", label="LOC", source="ner", confidence=0.88)
    d = span.model_dump()
    restored = Span.model_validate(d)
    assert restored == span


def test_span_json_roundtrip() -> None:
    span = Span(start=0, end=4, text="Roma", label="LOC", source="gliner")
    json_str = span.model_dump_json()
    restored = Span.model_validate_json(json_str)
    assert restored == span


# ---------------------------------------------------------------------------
# RedactionResult — valid construction
# ---------------------------------------------------------------------------


def test_redaction_result_valid() -> None:
    span = Span(start=0, end=5, text="Mario", label="PERSONA", source="regex")
    result = RedactionResult(original_text="Mario Rossi", redacted_text="[OSCURATO] Rossi", entities=[span])
    assert len(result.entities) == 1


def test_redaction_result_empty_entities() -> None:
    result = RedactionResult(original_text="testo senza PII", redacted_text="testo senza PII", entities=[])
    assert result.entities == []


def test_redaction_result_entities_default_empty() -> None:
    result = RedactionResult(original_text="x", redacted_text="x")
    assert result.entities == []


def test_redaction_result_redacted_text_can_be_empty_string() -> None:
    result = RedactionResult(original_text="Mario", redacted_text="", entities=[])
    assert result.redacted_text == ""


# ---------------------------------------------------------------------------
# RedactionResult — invalid construction
# ---------------------------------------------------------------------------


def test_redaction_result_empty_original_raises() -> None:
    with pytest.raises(ValidationError):
        RedactionResult(original_text="", redacted_text="", entities=[])


# ---------------------------------------------------------------------------
# RedactionResult — serialization round-trip
# ---------------------------------------------------------------------------


def test_redaction_result_serialization_roundtrip() -> None:
    span = Span(start=5, end=11, text="Rossi", label="PERSONA", source="ner", confidence=0.9)
    result = RedactionResult(
        original_text="Mario Rossi",
        redacted_text="Mario [OSCURATO]",
        entities=[span],
    )
    d = result.model_dump()
    restored = RedactionResult.model_validate(d)
    assert restored == result


def test_redaction_result_json_roundtrip() -> None:
    result = RedactionResult(original_text="test", redacted_text="test", entities=[])
    json_str = result.model_dump_json()
    restored = RedactionResult.model_validate_json(json_str)
    assert restored == result
