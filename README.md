# testrepo

Events system with pure synthetic event support.

## Overview

This repository implements an events system that supports various event types, including pure synthetic events. Pure synthetic events are programmatically generated system events used for automated actions and internal state tracking.

## Installation

```bash
pip install -r requirements.txt
```

## Features

- **Event Type System**: Support for multiple event types including text, tool calls, and pure synthetic events
- **Factory Pattern**: Easy event creation using factory methods
- **Validation**: Built-in validation to ensure event integrity
- **Database Support**: PostgreSQL schema with constraints and indexes
- **Comprehensive Testing**: Unit and integration tests included

## Usage

### Creating a Pure Synthetic Event

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

### Validating Events

```python
from events import validate_pure_synthetic_event, ValidationError

try:
    validate_pure_synthetic_event(event)
    print("Event is valid")
except ValidationError as e:
    print(f"Validation failed: {e}")
```

## Project Structure

```
testrepo/
├── src/
│   └── events/
│       ├── __init__.py
│       ├── types.py          # Event type definitions
│       ├── models.py         # Event model class
│       ├── factory.py        # Event factory methods
│       └── validators.py     # Event validation logic
├── tests/
│   ├── unit/
│   │   └── test_events.py    # Unit tests
│   └── integration/
│       └── test_events_db.py # Integration tests
├── migrations/
│   └── 20251016_add_pure_synthetic_constraint.sql
└── docs/
    ├── events.md             # Event system documentation
    └── api.md                # API documentation
```

## Testing

Run all tests:

```bash
pytest tests/
```

Run unit tests only:

```bash
pytest tests/unit/
```

Run integration tests only:

```bash
pytest tests/integration/
```

## Database Migration

To apply the database constraints and indexes:

```bash
psql -d your_database -f migrations/20251016_add_pure_synthetic_constraint.sql
```

## Documentation

- [Events Documentation](docs/events.md) - Detailed documentation on the events system
- [API Documentation](docs/api.md) - API endpoint specifications

## Event Types

- `messages.tool_status` - Tool status updates
- `messages.tool_call` - Tool invocation events
- `messages.sandbox_creation` - Sandbox creation events
- `text` - Text messages
- `messages.tool_result` - Tool execution results
- `PURE_SYNTHETIC` - Pure synthetic events (programmatically generated)

## Contributing

1. Ensure all tests pass before submitting changes
2. Add tests for new functionality
3. Update documentation as needed
4. Follow the existing code style

## License

MIT
