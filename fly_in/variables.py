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


class Files_in_use(str, Enum):
    """Class that contains all the project inputted files."""

    DRONE_ICON = "sprites/drone.piskel"
    LINEAR_PATH = "test-files/easy/01_linear_path.txt"
    SIMPLE_FORK = "test-files/easy/02_simple_fork.txt"
    BASIC_CAPACITY = "test-files/easy/03_basic_capacity.txt"
    DEAD_END_TRAP = "test-files/medium/01_dead_end_trap.txt"
    CIRCULAR_LOOP = "test-files/medium/02_circular_loop.txt"
    PRIORITY_PUZZLE = "test-files/medium/03_priority_puzzle.txt"
    MAZE_NIGHTMARE = "test-files/hard/01_maze_nightmare.txt"
    CAPACITY_HELL = "test-files/hard/02_capacity_hell.txt"
    ULTIMATE_CHALLENGE = "test-files/hard/03_ultimate_challenge.txt"
    THE_IMPOSSIBLE_DREAM = "test-files/challenger/01_the_impossible_dream.txt"