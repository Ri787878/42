from pydantic import BaseModel, Field, model_validator
from typing import Tuple, Union
from enum import Enum
# , ValidationError

valid_hub = Union[Tuple[str, int, int], Tuple[str, int, int, list[str]]]


class Tags(Enum):
    """Available tags for a hub."""
    NORMAL = "normal"
    BLOCKED = "blocked",
    RESTRICTED = "restricted",
    PRIORITY = "priority"


class Zone_Network(BaseModel):
    nb_drones: int = Field(ge=1)
    start_hub: valid_hub
    end_hub: valid_hub
    hub: list[valid_hub]
    connection: list[tuple[str, str]] = Field()
    turn_cost: int = 1
    is_blocked: bool = False
    prioritized: bool = False

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

    def existing_tags(self, tags: list[str]) -> list[str]:
        existing_tags: list[str] = []
        for metadata in tags:
            if "zone" in metadata:
                existing_tags.append("zone")
            if "color" in metadata:
                existing_tags.append("color")
            if "max_drones" in metadata:
                existing_tags.append("hub")
            if "tags" in metadata:
                existing_tags.append("tags")
        return existing_tags

    def check_metadata(self, tags: list[str]) -> None:
        existing_metadata: list[str] = self.existing_tags(tags)

        if Tags.NORMAL in existing_metadata:
            self.turn_cost = 1
        if Tags.BLOCKED in existing_metadata:
            self.is_blocked = True
        if Tags.RESTRICTED in existing_metadata:
            self.turn_cost = 2
        if Tags.PRIORITY in existing_metadata:
            self.turn_cost = 1
            self.prioritized = True

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
                metadata_list: list[str] = hub[3]
                self.check_metadata(tag_list)
            else:
                checked_zones.append(hub[0])

    @model_validator(mode="after")
    def check_inputs(self) -> "Zone_Network":
        self.is_valid_hub(self.start_hub)
        self.is_valid_hub(self.end_hub)

        return self
