from pydantic import BaseModel, Field, model_validator
from typing import Tuple, Union
# , ValidationError

valid_hub = Union[Tuple[str, int, int], Tuple[str, int, int, list[str]]]


class Zone_Network(BaseModel):
    nb_drones: int = Field(ge=1)
    start_hub: valid_hub
    end_hub: valid_hub
    hub: list[valid_hub]
    connection: list[tuple[str, str]] = Field()

    def __init__(
        self,
        input_nb_drones,
        input_start_hub,
        input_end_hub,
        input_hub,
        input_connection
    ) -> None:

        super().__init__(
            nb_drones=input_nb_drones,
            start_hub=input_start_hub,
            end_hub=input_end_hub,
            hub=input_hub,
            connection=input_connection
        )

    def is_valid_hub(self, hub_list: list | tuple) -> None:
        checked_zones: list[str] = []

        for hub in hub_list:
            if "-" in hub[0] or " " in hub[0]:
                raise ValueError(
                    f"[ERROR] Hub {hub[0]} can't have ' ' or '-'.")

            if (hub[1] < 0) or (hub[2] < 0):
                raise ValueError(
                    f"[ERROR] Hub {hub[0]} coordenates are invalid"
                    f" ({hub[1]},{hub[2]}).")
            if len(hub) > 3:
                checked_metadata: list[str] = []
                for metadata in hub[3]:
                    if "zone" in metadata:
                        checked_metadata.append("zone")
                    if "color" in metadata:
                        checked_metadata.append("color")
                        pass
                    if "max_drones" in metadata:
                        checked_metadata.append("hub")
                        pass
                    if "tags" in metadata:
                        checked_metadata.append("tags")
                        pass

                pass
            else:
                checked_zones.append(hub[0])

    @model_validator(mode="after")
    def check_inputs(self) -> "Zone_Network":
        self.is_valid_hub(self.start_hub)
        self.is_valid_hub(self.end_hub)

        return self
