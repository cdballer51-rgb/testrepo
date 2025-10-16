from typing import Optional
from uuid import UUID, uuid4
from datetime import datetime, timezone


class Event:
    def __init__(
        self,
        type: str,
        synthetic: bool,
        role: str,
        message: dict,
        chat_id: int,
        parent_uuid: Optional[UUID] = None,
        sidechain_root_uuid: Optional[UUID] = None,
        event_metadata: Optional[dict] = None,
        version: str = "1.0",
        uuid: Optional[UUID] = None,
        created_at: Optional[datetime] = None
    ):
        self.uuid = uuid or uuid4()
        self.type = type
        self.synthetic = synthetic
        self.role = role
        self.message = message
        self.chat_id = chat_id
        self.parent_uuid = parent_uuid
        self.sidechain_root_uuid = sidechain_root_uuid
        self.event_metadata = event_metadata or {}
        self.version = version
        self.created_at = created_at or datetime.now(timezone.utc)

    def __repr__(self):
        return f"<Event(uuid={self.uuid}, type={self.type}, synthetic={self.synthetic})>"
