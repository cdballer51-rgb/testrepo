from typing import Optional
from uuid import UUID

from .models import Event
from .types import EventType


def create_pure_synthetic_event(
    chat_id: int,
    message: dict,
    role: str = "system",
    parent_uuid: Optional[UUID] = None,
    sidechain_root_uuid: Optional[UUID] = None,
    event_metadata: Optional[dict] = None
) -> Event:
    """
    Create a pure synthetic event.
    
    Args:
        chat_id: Chat ID this event belongs to
        message: JSONB message payload
        role: Event role (default: system)
        parent_uuid: Optional parent event UUID
        sidechain_root_uuid: Optional sidechain root UUID
        event_metadata: Optional metadata
    
    Returns:
        Created Event instance
    """
    if "type" not in message:
        message["type"] = "PURE_SYNTHETIC"
    
    event = Event(
        type=EventType.PURE_SYNTHETIC,
        synthetic=True,
        role=role,
        message=message,
        chat_id=chat_id,
        parent_uuid=parent_uuid,
        sidechain_root_uuid=sidechain_root_uuid,
        event_metadata=event_metadata,
        version="1.0"
    )
    
    return event
