# Events System Documentation

## Overview

The events system provides a framework for managing different types of events in the application. Events can be user-generated or synthetic (programmatically generated).

## Event Types

| Event Type | Description | Synthetic |
|------------|-------------|-----------|
| `messages.tool_status` | Tool status updates | Yes |
| `messages.tool_call` | Tool invocation events | Yes |
| `messages.sandbox_creation` | Sandbox creation events | Yes |
| `text` | Text messages | No |
| `messages.tool_result` | Tool execution results | Yes |
| `PURE_SYNTHETIC` | Pure synthetic events (programmatically generated) | Yes |

## Pure Synthetic Events

Pure synthetic events are system-generated events that are created programmatically rather than from user input. These events are always marked with `synthetic=true` and `type='PURE_SYNTHETIC'`.

### Characteristics

- **Type**: `PURE_SYNTHETIC`
- **Synthetic**: Always `true`
- **Role**: Typically `system`, but can be customized
- **Use Cases**: System notifications, automated actions, internal state tracking

### Creating Pure Synthetic Events

Use the `create_pure_synthetic_event` factory function to create these events:

```python
from events import create_pure_synthetic_event

event = create_pure_synthetic_event(
    chat_id=123,
    message={
        "type": "PURE_SYNTHETIC",
        "action": "system_notification",
        "metadata": {"key": "value"}
    }
)
```

### Parameters

- `chat_id` (int, required): The chat ID this event belongs to
- `message` (dict, required): JSONB message payload. Must contain at least a `type` key
- `role` (str, optional): Event role. Defaults to `"system"`
- `parent_uuid` (UUID, optional): UUID of parent event for hierarchical relationships
- `sidechain_root_uuid` (UUID, optional): Root UUID for sidechain events
- `event_metadata` (dict, optional): Additional metadata for the event

### Example Usage

#### Basic Pure Synthetic Event

```python
event = create_pure_synthetic_event(
    chat_id=456,
    message={
        "type": "PURE_SYNTHETIC",
        "action": "automated_task",
        "details": "Background job completed"
    }
)
```

#### With Parent Relationship

```python
parent_event = create_pure_synthetic_event(
    chat_id=789,
    message={"type": "PURE_SYNTHETIC", "action": "start_workflow"}
)

child_event = create_pure_synthetic_event(
    chat_id=789,
    message={"type": "PURE_SYNTHETIC", "action": "workflow_step_1"},
    parent_uuid=parent_event.uuid
)
```

#### With Custom Metadata

```python
event = create_pure_synthetic_event(
    chat_id=101,
    message={"type": "PURE_SYNTHETIC", "data": "test"},
    event_metadata={
        "source": "background_worker",
        "priority": "high",
        "timestamp": "2025-10-16T12:00:00Z"
    }
)
```

## Validation

All pure synthetic events are validated to ensure:

1. The `synthetic` flag is set to `true`
2. The message contains required keys (at minimum, `type`)

Validation is performed using the `validate_pure_synthetic_event` function:

```python
from events import validate_pure_synthetic_event, ValidationError

try:
    validate_pure_synthetic_event(event)
except ValidationError as e:
    print(f"Validation failed: {e}")
```

## Database Schema

Pure synthetic events are stored in the `events` table with the following relevant columns:

- `uuid`: Unique identifier (UUID)
- `type`: Event type (`PURE_SYNTHETIC`)
- `synthetic`: Boolean flag (always `true`)
- `role`: Event role
- `message`: JSONB message payload
- `chat_id`: Associated chat ID
- `parent_uuid`: Optional parent event UUID
- `sidechain_root_uuid`: Optional sidechain root UUID
- `event_metadata`: Optional JSONB metadata
- `version`: Event schema version
- `created_at`: Timestamp of creation

### Database Constraints

A database constraint ensures that all events with `type='PURE_SYNTHETIC'` must have `synthetic=true`:

```sql
ALTER TABLE events 
ADD CONSTRAINT check_pure_synthetic_is_synthetic
CHECK (type != 'PURE_SYNTHETIC' OR synthetic = true);
```

### Indexes

An index is created for efficient querying of synthetic events:

```sql
CREATE INDEX IF NOT EXISTS idx_events_type_synthetic 
ON events(type, synthetic) 
WHERE synthetic = true;
```

## Querying Pure Synthetic Events

### By Type

```python
pure_synthetic_events = db_session.query(Event).filter_by(
    type=EventType.PURE_SYNTHETIC
).all()
```

### By Chat ID

```python
chat_events = db_session.query(Event).filter_by(
    chat_id=123,
    type=EventType.PURE_SYNTHETIC
).all()
```

### All Synthetic Events

```python
all_synthetic = db_session.query(Event).filter_by(
    synthetic=True
).all()
```

## Error Handling

### ValidationError

Raised when an event fails validation:

```python
from events import ValidationError

try:
    event = Event(type="PURE_SYNTHETIC", synthetic=False, ...)
    validate_pure_synthetic_event(event)
except ValidationError as e:
    print(f"Validation error: {e}")
```

Common validation errors:

- `PURE_SYNTHETIC events must have synthetic=True`: The event type is `PURE_SYNTHETIC` but `synthetic` is `false`
- `Message missing required keys`: The message dictionary is missing required fields

## Best Practices

1. **Always use the factory function**: Use `create_pure_synthetic_event()` instead of manually constructing `Event` objects to ensure proper initialization
2. **Include meaningful message data**: Structure the message payload to include actionable information
3. **Use parent relationships**: Link related events using `parent_uuid` for better traceability
4. **Add metadata**: Use `event_metadata` for additional context that doesn't belong in the message payload
5. **Validate before persisting**: Call `validate_pure_synthetic_event()` before saving to the database to catch errors early

## Migration

To apply the database constraints and indexes, run the migration:

```bash
psql -d your_database -f migrations/20251016_add_pure_synthetic_constraint.sql
```

## Testing

Unit tests are available in `tests/unit/test_events.py` and integration tests in `tests/integration/test_events_db.py`.

Run tests with:

```bash
pytest tests/
```
