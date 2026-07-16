from models.drones import Drone
from pathfinder.pathfinder import Pathfinder
from models.zone_network import Zone_Network


class Dispatcher():
    def dispatch_drones(self, network: Zone_Network) -> list[Drone]:
        """
        Build one route per drone.
        Occupied hubs increase routing cost, but do not fully block paths.
        """

        occupied_hubs: dict[str, int] = {}
        drones: list[Drone] = []
        pathfinder = Pathfinder()

        for _ in range(network.nb_drones):
            route = pathfinder.pathfinder(network, occupied_hubs=occupied_hubs)
            drone = Drone.build_drone(network, route)
            drones.append(drone)

            for hub in route[1:-1]:
                occupied_hubs[hub.name] = occupied_hubs.get(hub.name, 0) + 1

        return drones
