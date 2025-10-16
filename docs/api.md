# API Documentation

## Events API

### POST /events

Create a new event.

#### Request Body

```json
{
  "type": "PURE_SYNTHETIC",
  "synthetic": true,
  "role": "system",
  "message": {
    "type": "PURE_SYNTHETIC",
    "action": "example_action",
    "data": "example data"
  },
  "chat_id": 123,
  "parent_uuid": "12345678-1234-5678-1234-567812345678",
  "event_metadata": {
    "key": "value"
  }
}
```

#### Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `type` | string | Yes | Event type. Valid values: `messages.tool_status`, `messages.tool_call`, `messages.sandbox_creation`, `text`, `messages.tool_result`, `PURE_SYNTHETIC` |
| `synthetic` | boolean | Yes | Whether the event is synthetic (programmatically generated) |
| `role` | string | Yes | Event role (e.g., `system`, `user`, `assistant`) |
| `message` | object | Yes | JSONB message payload. Must contain at least a `type` key |
| `chat_id` | integer | Yes | Chat ID this event belongs to |
| `parent_uuid` | string (UUID) | No | Optional parent event UUID for hierarchical relationships |
| `sidechain_root_uuid` | string (UUID) | No | Optional sidechain root UUID |
| `event_metadata` | object | No | Optional metadata object |

#### Response

```json
{
  "uuid": "87654321-4321-8765-4321-876543218765",
  "type": "PURE_SYNTHETIC",
  "synthetic": true,
  "role": "system",
  "message": {
    "type": "PURE_SYNTHETIC",
    "action": "example_action",
    "data": "example data"
  },
  "chat_id": 123,
  "parent_uuid": "12345678-1234-5678-1234-567812345678",
  "event_metadata": {
    "key": "value"
  },
  "version": "1.0",
  "created_at": "2025-10-16T12:00:00.000Z"
}
```

#### Status Codes

- `201 Created`: Event successfully created
- `400 Bad Request`: Invalid request body or validation error
- `422 Unprocessable Entity`: Event validation failed

#### Validation Rules for PURE_SYNTHETIC Events

1. `synthetic` must be `true`
2. `message` must contain a `type` key
3. `type` must be `"PURE_SYNTHETIC"`

#### Example: Create Pure Synthetic Event

```bash
curl -X POST http://api.example.com/events \
  -H "Content-Type: application/json" \
  -d '{
    "type": "PURE_SYNTHETIC",
    "synthetic": true,
    "role": "system",
    "message": {
      "type": "PURE_SYNTHETIC",
      "action": "automated_notification",
      "details": "System update completed"
    },
    "chat_id": 456
  }'
```

### GET /events

Retrieve events with optional filters.

#### Query Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `chat_id` | integer | Filter by chat ID |
| `type` | string | Filter by event type |
| `synthetic` | boolean | Filter by synthetic flag |
| `parent_uuid` | string (UUID) | Filter by parent UUID |
| `limit` | integer | Maximum number of results (default: 100) |
| `offset` | integer | Pagination offset (default: 0) |

#### Example: Get Pure Synthetic Events

```bash
curl -X GET "http://api.example.com/events?type=PURE_SYNTHETIC&synthetic=true"
```

#### Response

```json
{
  "events": [
    {
      "uuid": "87654321-4321-8765-4321-876543218765",
      "type": "PURE_SYNTHETIC",
      "synthetic": true,
      "role": "system",
      "message": {
        "type": "PURE_SYNTHETIC",
        "action": "example_action"
      },
      "chat_id": 123,
      "created_at": "2025-10-16T12:00:00.000Z"
    }
  ],
  "total": 1,
  "limit": 100,
  "offset": 0
}
```

### GET /events/:uuid

Retrieve a specific event by UUID.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `uuid` | string (UUID) | Event UUID |

#### Response

```json
{
  "uuid": "87654321-4321-8765-4321-876543218765",
  "type": "PURE_SYNTHETIC",
  "synthetic": true,
  "role": "system",
  "message": {
    "type": "PURE_SYNTHETIC",
    "action": "example_action"
  },
  "chat_id": 123,
  "parent_uuid": null,
  "sidechain_root_uuid": null,
  "event_metadata": {},
  "version": "1.0",
  "created_at": "2025-10-16T12:00:00.000Z"
}
```

#### Status Codes

- `200 OK`: Event found
- `404 Not Found`: Event not found

## Error Responses

### Validation Error

```json
{
  "error": "ValidationError",
  "message": "PURE_SYNTHETIC events must have synthetic=True",
  "code": "VALIDATION_FAILED"
}
```

### Not Found

```json
{
  "error": "NotFound",
  "message": "Event not found",
  "code": "EVENT_NOT_FOUND"
}
```

### Bad Request

```json
{
  "error": "BadRequest",
  "message": "Invalid request body: missing required field 'chat_id'",
  "code": "INVALID_REQUEST"
}
```
