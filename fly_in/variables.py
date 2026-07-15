from enum import Enum


class Approved_tags(str, Enum):
    """Approved tags as individual Enum members."""
    NORMAL = "normal"
    BLOCKED = "blocked"
    RESTRICTED = "restricted"
    PRIORITY = "priority"


class DroneStatus(str, Enum):
    """Runtime state for a drone."""
    IDLE = "idle"
    MOVING = "moving"
    ARRIVED = "arrived"
    BLOCKED = "blocked"
