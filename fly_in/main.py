from pydantic import ValidationError
import sys

from dispatcher import dispatch_drones
from error_handling import InvalidConfiguration
from pathfinder.pathfinder import pathfinder
from ui.pygame_display import start_display
from zone_network import Zone_Network


def main() -> None:
    try:
        if len(sys.argv) != 2:
            print("[ERROR] No valid map was issued.")
            sys.exit(1)

        network = Zone_Network.from_file(sys.argv[1])

        drones = dispatch_drones(network)

        start_display(network, drones)

    except (InvalidConfiguration, ValidationError) as e:
        print(f"Configuration Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
