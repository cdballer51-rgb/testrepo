from enum import Enum


class EventType(str, Enum):
    TOOL_STATUS = "messages.tool_status"
    TOOL_CALL = "messages.tool_call"
    SANDBOX_CREATION = "messages.sandbox_creation"
    TEXT = "text"
    TOOL_RESULT = "messages.tool_result"
    PURE_SYNTHETIC = "PURE_SYNTHETIC"
