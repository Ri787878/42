from __future__ import annotations

from heapq import heappop, heappush

from zone_network import Hub, Zone_Network


def _heuristic(current: Hub, goal: Hub) -> int:
    return (abs(current.x_coord - goal.x_coord) +
            abs(current.y_coord - goal.y_coord))


def _reconstruct_path(
    came_from: dict[str, str],
    hub_map: dict[str, Hub],
    current_name: str,
) -> list[Hub]:
    path = [hub_map[current_name]]

    while current_name in came_from:
        current_name = came_from[current_name]
        path.append(hub_map[current_name])

    path.reverse()
    return path


def pathfinder(
    network: Zone_Network,
    occupied_hubs: dict[str, int] | None = None,
) -> list[Hub]:
    occupied_hubs = occupied_hubs or {}

    start_hub = network.start_hub
    goal_hub = network.end_hub

    if start_hub.is_blocked:
        raise ValueError("[ERROR] Start hub is blocked.")
    if goal_hub.is_blocked:
        raise ValueError("[ERROR] End hub is blocked.")

    open_set: list[tuple[int, int, int, str, Hub]] = []
    came_from: dict[str, str] = {}
    g_score: dict[str, int] = {start_hub.name: 0}

    start_priority = 0 if start_hub.prefered_zone else 1
    heappush(
        open_set,
        (
            _heuristic(start_hub, goal_hub),
            start_priority,
            0,
            start_hub.name,
            start_hub,
        ),
    )

    while open_set:
        _, _, current_cost, _, current_hub = heappop(open_set)

        if current_hub.name == goal_hub.name:
            return _reconstruct_path(
                came_from,
                network.hub_map,
                current_hub.name)

        if current_cost > g_score.get(current_hub.name, current_cost):
            continue

        for neighbor in network.neighbors(current_hub.name):
            if neighbor.is_blocked:
                continue

            congestion = occupied_hubs.get(neighbor.name, 0)
            congestion_penalty = congestion * 5

            tentative_cost = (
                current_cost +
                neighbor.movement_cost +
                congestion_penalty)

            if tentative_cost >= g_score.get(neighbor.name, float("inf")):
                continue

            came_from[neighbor.name] = current_hub.name
            g_score[neighbor.name] = tentative_cost

            priority_score = 0 if neighbor.prefered_zone else 1
            total_score = tentative_cost + _heuristic(neighbor, goal_hub)

            heappush(
                open_set,
                (
                    total_score,
                    priority_score,
                    tentative_cost,
                    neighbor.name,
                    neighbor,
                ),
            )

    raise ValueError("[ERROR] No valid path was found.")
