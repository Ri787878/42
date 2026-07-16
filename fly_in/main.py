from pydantic import ValidationError
import sys
import copy

from pathfinder import Dispatcher
from output_logs import Logger
from ui import Displayer, Map_Selector
from models import Zone_Network, InvalidConfiguration


"""
def main() -> None:
    try:
        if len(sys.argv) != 2:
            print("[ERROR] No valid map was issued.")
            sys.exit(1)

        displayer = Displayer()
        dispatcher = Dispatcher()
        logger = Logger()

        network = Zone_Network.from_file(sys.argv[1])
        drones = dispatcher.dispatch_drones(network)

        display_drones = copy.deepcopy(drones)

        history = logger.simulate_drones(network, drones)

        displayer.start_display(network, display_drones, history)

    except (InvalidConfiguration, ValidationError) as e:
        print(f"Configuration Error: {e}")
        sys.exit(1)
"""


def main() -> None:
    Map_Selector.select_map()


if __name__ == "__main__":
    main()
