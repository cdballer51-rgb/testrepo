import pytest
from uuid import UUID

import sys
sys.path.insert(0, '/home/ubuntu/repos/testrepo/src')

from events import (
    Event,
    EventType,
    create_pure_synthetic_event,
    validate_pure_synthetic_event,
    ValidationError
)


def test_create_pure_synthetic_event():
    event = create_pure_synthetic_event(
        chat_id=1,
        message={"type": "PURE_SYNTHETIC", "data": "test"}
    )
    assert event.type == EventType.PURE_SYNTHETIC
    assert event.synthetic is True
    assert event.role == "system"
    assert event.chat_id == 1
    assert event.message["type"] == "PURE_SYNTHETIC"
    assert event.message["data"] == "test"
    assert event.version == "1.0"


def test_create_pure_synthetic_event_auto_adds_type():
    event = create_pure_synthetic_event(
        chat_id=2,
        message={"data": "test without type"}
    )
    assert event.message["type"] == "PURE_SYNTHETIC"


def test_create_pure_synthetic_event_with_custom_role():
    event = create_pure_synthetic_event(
        chat_id=3,
        message={"type": "PURE_SYNTHETIC"},
        role="assistant"
    )
    assert event.role == "assistant"


def test_create_pure_synthetic_event_with_parent_uuid():
    parent_id = UUID("12345678-1234-5678-1234-567812345678")
    event = create_pure_synthetic_event(
        chat_id=4,
        message={"type": "PURE_SYNTHETIC"},
        parent_uuid=parent_id
    )
    assert event.parent_uuid == parent_id


def test_create_pure_synthetic_event_with_metadata():
    metadata = {"key": "value", "count": 42}
    event = create_pure_synthetic_event(
        chat_id=5,
        message={"type": "PURE_SYNTHETIC"},
        event_metadata=metadata
    )
    assert event.event_metadata == metadata


def test_pure_synthetic_validation_passes():
    event = Event(
        type=EventType.PURE_SYNTHETIC,
        synthetic=True,
        role="system",
        message={"type": "PURE_SYNTHETIC", "data": "test"},
        chat_id=1
    )
    assert validate_pure_synthetic_event(event) is True


def test_pure_synthetic_validation_fails_when_not_synthetic():
    event = Event(
        type=EventType.PURE_SYNTHETIC,
        synthetic=False,
        role="system",
        message={"type": "PURE_SYNTHETIC"},
        chat_id=1
    )
    with pytest.raises(ValidationError) as exc_info:
        validate_pure_synthetic_event(event)
    assert "must have synthetic=True" in str(exc_info.value)


def test_pure_synthetic_validation_fails_missing_required_keys():
    event = Event(
        type=EventType.PURE_SYNTHETIC,
        synthetic=True,
        role="system",
        message={},
        chat_id=1
    )
    with pytest.raises(ValidationError) as exc_info:
        validate_pure_synthetic_event(event)
    assert "missing required keys" in str(exc_info.value)


def test_validation_passes_for_non_pure_synthetic_events():
    event = Event(
        type=EventType.TEXT,
        synthetic=False,
        role="user",
        message={"content": "hello"},
        chat_id=1
    )
    assert validate_pure_synthetic_event(event) is True


def test_event_has_uuid():
    event = create_pure_synthetic_event(
        chat_id=6,
        message={"type": "PURE_SYNTHETIC"}
    )
    assert isinstance(event.uuid, UUID)


def test_event_has_created_at():
    event = create_pure_synthetic_event(
        chat_id=7,
        message={"type": "PURE_SYNTHETIC"}
    )
    assert event.created_at is not None
