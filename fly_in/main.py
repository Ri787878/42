from zone_network import Zone_Network
from error_handling import InvalidConfiguration
from pathfinder.pathfinder import pathfinder
# from drones import Drone, DroneStatus
from pydantic import ValidationError
from ui.pygame_display import start_display
import sys


def main() -> None:

    try:
        """start_hub = Hub(
            name="start",
            x_coord=0,
            y_coord=0,
            metadata=["color=green"]
        )"""

        if len(sys.argv) != 2:
            print("[ERROR] No valid map was issued.")
            sys.exit(1)

        network = Zone_Network.from_file(sys.argv[1])
        print(f"connections: {network.connection}")

        route = pathfinder(network)

        start_display(network, route)

    except (InvalidConfiguration, ValidationError) as e:
        print(f"Configuration Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
    # start_display()
