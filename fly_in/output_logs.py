from __future__ import annotations

from collections import deque
from typing import TypedDict

from drones import Drone
from zone_network import Hub, Zone_Network


class ActiveDrone(TypedDict):
    id: int
    drone: Drone
    path_index: int


def _is_restricted(hub: Hub) -> bool:
    return hub.zone == "restricted"


def _movement_label(
    network: Zone_Network,
    current_hub: Hub,
    next_hub: Hub,
) -> str:
    if _is_restricted(next_hub):
        c_name, n_name = current_hub.name, next_hub.name
        for left, right in network.connection:
            if {left, right} == {c_name, n_name}:
                return right if right == n_name else left
        return n_name

    return next_hub.name


def _hub_has_capacity(hub: Hub, occupied_count: int) -> bool:
    return hub.max_drones is None or occupied_count < hub.max_drones


def simulate_drones(network: Zone_Network, drones: list[Drone]) -> None:
    active_drones: list[ActiveDrone] = [
        {
            "id": index + 1,
            "drone": drone,
            "path_index": 0,
        }
        for index, drone in enumerate(drones)
    ]
    queued_drones = deque[ActiveDrone]()

    start_hub = network.start_hub
    # Handle start_capacity safely when max_drones is None
    start_capacity = (
        start_hub.max_drones
        if start_hub.max_drones is not None
        else float("inf")
    )

    if (
        start_hub.max_drones is not None
        and len(active_drones) > start_hub.max_drones
    ):
        queued_drones.extend(active_drones[start_hub.max_drones :])
        active_drones = active_drones[: start_hub.max_drones]

    occupancy: dict[str, int] = {start_hub.name: len(active_drones)}

    while active_drones or queued_drones:
        # Fill starting vacancies from the queue
        while (
            queued_drones
            and occupancy.get(start_hub.name, 0) < start_capacity
        ):
            item = queued_drones.popleft()
            active_drones.append(item)
            occupancy[start_hub.name] = occupancy.get(start_hub.name, 0) + 1

        turn_movements: list[str] = []
        delivered_ids: list[int] = []
        any_movement_occurred = False  # Track if any progress is made

        for item in active_drones:
            drone_id = item["id"]
            drone: Drone = item["drone"]
            path_index = item["path_index"]
            path = drone.planned_path

            if path_index >= len(path) - 1:
                delivered_ids.append(drone_id)
                continue

            current_hub = path[path_index]
            next_hub = path[path_index + 1]

            # Use helper function to check capacity limits safely
            next_occupancy = occupancy.get(next_hub.name, 0)
            if not _hub_has_capacity(next_hub, next_occupancy):
                continue

            # A valid movement is about to happen!
            any_movement_occurred = True

            occupancy[current_hub.name] -= 1
            occupancy[next_hub.name] = occupancy.get(next_hub.name, 0) + 1

            movement_name = _movement_label(network, current_hub, next_hub)
            turn_movements.append(f"D{drone_id}-{movement_name}")

            item["path_index"] = path_index + 1
            drone.current_hub = next_hub

            if item["path_index"] >= len(path) - 1:
                delivered_ids.append(drone_id)

        # Print progress if movements occurred
        if turn_movements:
            print(" ".join(turn_movements))

        # Filter out finished drones
        active_drones = [
            item for item in active_drones if item["id"] not in delivered_ids
        ]

        # DEADLOCK SAFEGUARD: Prevent infinite loops if simulation stalls
        if (active_drones or queued_drones) and not any_movement_occurred:
            print("[WARNING] Simulation stalled! No drones can progress.")
            break
