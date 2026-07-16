from pydantic import ValidationError
import sys
import copy

from dispatcher import dispatch_drones
from output_logs import simulate_drones
# from drones import Drone
from error_handling import InvalidConfiguration
from ui.pygame_display import start_display
from zone_network import Zone_Network


def main() -> None:
    try:
        if len(sys.argv) != 2:
            print("[ERROR] No valid map was issued.")
            sys.exit(1)

        network = Zone_Network.from_file(sys.argv[1])
        drones = dispatch_drones(network)

        display_drones = copy.deepcopy(drones)

        history = simulate_drones(network, drones)

        start_display(network, display_drones, history)

    except (InvalidConfiguration, ValidationError) as e:
        print(f"Configuration Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
