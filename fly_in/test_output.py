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


def simulate_drones(network: Zone_Network, drones: list[Drone]) -> None:
    active_drones: list[ActiveDrone] = [
        {
            "id": index + 1,
            "drone": drone,
            "path_index": 0,
        }
        for index, drone in enumerate(drones)
    ]
    queued_drones: deque[ActiveDrone] = deque()

    start_hub = network.start_hub
    start_capacity = start_hub.max_drones

    if len(active_drones) > start_capacity:
        queued_drones.extend(active_drones[start_capacity:])
        active_drones = active_drones[:start_capacity]

    occupancy: dict[str, int] = {start_hub.name: len(active_drones)}

    while active_drones or queued_drones:
        still_active: list[ActiveDrone] = []
        for item in active_drones:
            drone: Drone = item["drone"]
            path = drone.planned_path

            if item["path_index"] >= len(path) - 1:
                current_hub = drone.current_hub
                occupancy[current_hub.name] -= 1
                continue

            still_active.append(item)

        active_drones = still_active

        while (
            queued_drones
            and occupancy.get(start_hub.name, 0) < start_capacity
        ):
            item = queued_drones.popleft()
            active_drones.append(item)
            occupancy[start_hub.name] = occupancy.get(start_hub.name, 0) + 1

        turn_movements: list[str] = []
        delivered_ids: list[int] = []

        for item in active_drones:
            drone_id = item["id"]
            drone = item["drone"]
            path_index = item["path_index"]
            path = drone.planned_path

            if path_index >= len(path) - 1:
                delivered_ids.append(drone_id)
                continue

            current_hub = path[path_index]
            next_hub = path[path_index + 1]

            if occupancy.get(next_hub.name, 0) >= next_hub.max_drones:
                continue

            occupancy[current_hub.name] -= 1
            occupancy[next_hub.name] = occupancy.get(next_hub.name, 0) + 1

            movement_name = _movement_label(network, current_hub, next_hub)
            turn_movements.append(f"D{drone_id}-{movement_name}")

            item["path_index"] = path_index + 1
            drone.current_hub = next_hub

            if item["path_index"] >= len(path) - 1:
                delivered_ids.append(drone_id)

        if turn_movements:
            print(" ".join(turn_movements))

        active_drones = [
            item for item in active_drones if item["id"] not in delivered_ids
        ]
