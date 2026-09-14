from pydantic import ValidationError
import sys
import copy

from pathfinder import Dispatcher, Pathfinder
from log_handling import Logger
from ui import Displayer, Map_Selector
from models import Zone_Network, InvalidConfiguration


def main() -> None:
    try:
        show_capacity = False
        
        if len(sys.argv) > 2:
            print("[ERROR] invalid number of arguments.")
            sys.exit(1)
        
        if len(sys.argv) == 2:
            if sys.argv[1] == "--capacity-info":
                show_capacity = True
            else:
                print(f"[ERROR] Unknown argument: {sys.argv[1]}")
                sys.exit(1)

        test_map: str = Map_Selector.select_map()

        if test_map == "":
            print("[ERROR] No valid map was issued.")
            sys.exit(1)

        displayer = Displayer()
        dispatcher = Dispatcher()
        logger = Logger()

        network = Zone_Network.from_file(test_map)
        drones = dispatcher.dispatch_drones(network)

        display_drones = copy.deepcopy(drones)

        pathfinder = Pathfinder()
        history = logger.simulate_drones(
            network,
            drones,
            pathfinder,
            show_capacity=show_capacity
        )

        displayer.start_display(network, display_drones, history)

    except ValidationError as e:
        message = e.errors()[0]["msg"]
        print(message.removeprefix("Value error, "))
        sys.exit(1)
    except InvalidConfiguration as e:
        print(str(e).removeprefix("Input Error: "))
        sys.exit(1)


if __name__ == "__main__":
    main()
