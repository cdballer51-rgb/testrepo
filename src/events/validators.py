from .models import Event
from .types import EventType


class ValidationError(Exception):
    pass


def validate_pure_synthetic_event(event: Event) -> bool:
    """Ensure PURE_SYNTHETIC events meet requirements."""
    if event.type == EventType.PURE_SYNTHETIC:
        if not event.synthetic:
            raise ValidationError("PURE_SYNTHETIC events must have synthetic=True")
        
        required_keys = ["type"]
        if not all(key in event.message for key in required_keys):
            raise ValidationError(f"Message missing required keys: {required_keys}")
    
    return True
