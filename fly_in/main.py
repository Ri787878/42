from zone_network import Zone_Network, InvalidConfiguration
from pydantic import ValidationError
import sys


def main() -> None:

    try:
        """start_hub = Hub(
            name="start",
            x_coord=0,
            y_coord=0,
            metadata=["color=green"]
        )"""

        network = Zone_Network.from_file(sys.argv[1])

        # Access attributes cleanly via dot notation instead of dict keys
        print(f"nb_drones: {network.nb_drones}")
        print(f"Start hub has conf: {network.start_hub}")
        print(f"End hub has conf: {network.end_hub}")

        for h in network.hub:
            print(f"This hub has conf: {h}")

    except (InvalidConfiguration, ValidationError) as e:
        print(f"Configuration Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
