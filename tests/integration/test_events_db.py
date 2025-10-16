import pytest
from uuid import UUID

import sys
sys.path.insert(0, '/home/ubuntu/repos/testrepo/src')

from events import (
    Event,
    EventType,
    create_pure_synthetic_event,
    validate_pure_synthetic_event
)


class MockDBSession:
    """Mock database session for integration testing."""
    
    def __init__(self):
        self.objects = []
    
    def add(self, obj):
        self.objects.append(obj)
    
    def commit(self):
        pass
    
    def query(self, model):
        return MockQuery(self.objects, model)


class MockQuery:
    """Mock query object for filtering."""
    
    def __init__(self, objects, model):
        self.objects = [obj for obj in objects if isinstance(obj, model)]
        self.filters = {}
    
    def filter_by(self, **kwargs):
        filtered = []
        for obj in self.objects:
            match = True
            for key, value in kwargs.items():
                if not hasattr(obj, key) or getattr(obj, key) != value:
                    match = False
                    break
            if match:
                filtered.append(obj)
        
        result = MockQuery([], type(self.objects[0])) if self.objects else MockQuery([], Event)
        result.objects = filtered
        return result
    
    def first(self):
        return self.objects[0] if self.objects else None
    
    def all(self):
        return self.objects


@pytest.fixture
def db_session():
    return MockDBSession()


def test_insert_pure_synthetic_event_to_db(db_session):
    event = create_pure_synthetic_event(
        chat_id=1,
        message={"type": "PURE_SYNTHETIC", "action": "test"}
    )
    
    validate_pure_synthetic_event(event)
    
    db_session.add(event)
    db_session.commit()
    
    result = db_session.query(Event).filter_by(
        type=EventType.PURE_SYNTHETIC
    ).first()
    
    assert result is not None
    assert result.synthetic is True
    assert result.type == EventType.PURE_SYNTHETIC
    assert result.chat_id == 1


def test_query_pure_synthetic_events_by_chat_id(db_session):
    event1 = create_pure_synthetic_event(
        chat_id=1,
        message={"type": "PURE_SYNTHETIC", "data": "event1"}
    )
    event2 = create_pure_synthetic_event(
        chat_id=1,
        message={"type": "PURE_SYNTHETIC", "data": "event2"}
    )
    event3 = create_pure_synthetic_event(
        chat_id=2,
        message={"type": "PURE_SYNTHETIC", "data": "event3"}
    )
    
    db_session.add(event1)
    db_session.add(event2)
    db_session.add(event3)
    db_session.commit()
    
    results = db_session.query(Event).filter_by(
        chat_id=1,
        type=EventType.PURE_SYNTHETIC
    ).all()
    
    assert len(results) == 2
    assert all(e.chat_id == 1 for e in results)
    assert all(e.type == EventType.PURE_SYNTHETIC for e in results)


def test_insert_multiple_event_types(db_session):
    pure_synthetic = create_pure_synthetic_event(
        chat_id=1,
        message={"type": "PURE_SYNTHETIC"}
    )
    
    text_event = Event(
        type=EventType.TEXT,
        synthetic=False,
        role="user",
        message={"content": "Hello"},
        chat_id=1
    )
    
    db_session.add(pure_synthetic)
    db_session.add(text_event)
    db_session.commit()
    
    pure_results = db_session.query(Event).filter_by(
        type=EventType.PURE_SYNTHETIC
    ).all()
    
    text_results = db_session.query(Event).filter_by(
        type=EventType.TEXT
    ).all()
    
    assert len(pure_results) == 1
    assert pure_results[0].synthetic is True
    
    assert len(text_results) == 1
    assert text_results[0].synthetic is False


def test_event_with_parent_relationship(db_session):
    parent_event = create_pure_synthetic_event(
        chat_id=1,
        message={"type": "PURE_SYNTHETIC", "data": "parent"}
    )
    
    db_session.add(parent_event)
    db_session.commit()
    
    child_event = create_pure_synthetic_event(
        chat_id=1,
        message={"type": "PURE_SYNTHETIC", "data": "child"},
        parent_uuid=parent_event.uuid
    )
    
    db_session.add(child_event)
    db_session.commit()
    
    result = db_session.query(Event).filter_by(
        parent_uuid=parent_event.uuid
    ).first()
    
    assert result is not None
    assert result.parent_uuid == parent_event.uuid
    assert result.message["data"] == "child"


def test_query_synthetic_events(db_session):
    synthetic1 = create_pure_synthetic_event(
        chat_id=1,
        message={"type": "PURE_SYNTHETIC"}
    )
    
    synthetic2 = Event(
        type=EventType.SANDBOX_CREATION,
        synthetic=True,
        role="system",
        message={"type": "sandbox"},
        chat_id=1
    )
    
    non_synthetic = Event(
        type=EventType.TEXT,
        synthetic=False,
        role="user",
        message={"content": "user message"},
        chat_id=1
    )
    
    db_session.add(synthetic1)
    db_session.add(synthetic2)
    db_session.add(non_synthetic)
    db_session.commit()
    
    all_events = db_session.query(Event).all()
    synthetic_events = [e for e in all_events if e.synthetic]
    
    assert len(all_events) == 3
    assert len(synthetic_events) == 2
    assert all(e.synthetic for e in synthetic_events)
