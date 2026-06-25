from zone_network import Hub, InvalidConfiguration
from pydantic import ValidationError
from parser.parcer import file_interpreter
import sys

if __name__ == "__main__":

    try:
        start_hub = Hub(
            name="start",
            x_coord=0,
            y_coord=0,
            metadata=["color=green"]
        )

        # print(start_hub.color)
        # print(start_hub.zone)
        # print(start_hub.x_coord)

        project_configuration: dict = file_interpreter(sys.argv[1])
        # print(project_configuration)

        # Fixed: Outer double quotes, inner single quotes
        print(f"Start hub has conf:{project_configuration['start_hub']}")
        print(f"End hub has conf:{project_configuration['end_hub']}")

        for hub in project_configuration["hubs"]:
            print(f"This hub has conf:{hub}")

    except (InvalidConfiguration, ValidationError) as e:
        print(e)
