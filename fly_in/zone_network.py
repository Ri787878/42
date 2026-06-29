from pathlib import Path
from typing_extensions import Self
from pydantic import BaseModel, Field, model_validator
from enum import Enum
# , ValidationError


class Approved_tags(str, Enum):
    """Approved tags as individual Enum members."""
    NORMAL = "normal"
    BLOCKED = "blocked"
    RESTRICTED = "restricted"
    PRIORITY = "priority"


class InvalidConfiguration(Exception):
    def __init__(self, error: str) -> None:
        super().__init__(f"Input Error: {error}")


class Hub(BaseModel):
    """Represents a Hub"""
    # Inputted Values
    name: str = Field(min_length=1)
    x_coord: int = Field()
    y_coord: int = Field()
    metadata: list[str] | None = None

    # Base Hidden values
    movement_cost: int = Field(default=1)
    is_blocked: bool = Field(default=False)
    prefered_zone: bool = Field(default=False)

    # Metadata
    zone: str = Field(default="normal")
    color: str = Field(default="white")
    max_drones: int = Field(default=1)

    @model_validator(mode="after")
    def validate_hub(self) -> "Hub":
        # Check Errors in Inputed values
        if "-" in self.name or " " in self.name:
            raise InvalidConfiguration(
                f"[ERROR] Hub {self.name} can't have ' ' or '-'.")
        if " " in self.color:
            raise InvalidConfiguration(
                f"[ERROR] Hub {self.name} can't have multi word colors"
                f" '{self.color}'.")

        # Apply configurations depending on existing Metadata
        self.apply_metadata()
        self.apply_zone_qualifiers()

        return self

    def apply_metadata(self) -> None:
        if not self.metadata:
            return
        else:
            for metadata in self.metadata:
                if metadata.startswith("zone"):
                    if metadata[5:] in [tag.value for tag in Approved_tags]:
                        self.zone = metadata[5:]
                    else:
                        raise InvalidConfiguration(
                            f"[ERROR] Hub '{self.name}'"
                            f" has invalid zone '{metadata[5:]}'.")
                elif "color" in metadata:
                    self.color = metadata[6:]
                elif "max_drones" in metadata:
                    self.max_drones = int(metadata[11:])

    def apply_zone_qualifiers(self) -> None:
        if self.zone == "normal":
            pass
        elif self.zone == "blocked":
            self.is_blocked = True
        elif self.zone == "restricted":
            self.movement_cost = 2
        elif self.zone == "priority":
            self.movement_cost = 1
            self.prefered_zone = True


class Zone_Network(BaseModel):
    nb_drones: int = Field(ge=1)
    start_hub: Hub
    end_hub: Hub
    hub: list[Hub] = Field(default_factory=list)
    connection: list[tuple[str, str]] = Field(default_factory=list)

    @model_validator(mode="after")
    def check_inputs(self) -> "Zone_Network":
        # Check if start and end hubs are in the exact same spot
        if (self.start_hub.x_coord == self.end_hub.x_coord and
                self.start_hub.y_coord == self.end_hub.y_coord):
            raise ValueError(
                "[ERROR] Start hub and End hub cannot"
                " share the same coordinates.")
        return self

    @classmethod
    def from_file(cls, filename: str | Path) -> Self:
        """
        Parses a configuration file and initializes a Zone_Network instance.
        """
        with open(filename, "r") as f:
            content = f.read()

        lines: list[str] = content.splitlines()

        # Raw parsed strings/lists from file
        nb_drones_str: str = ""
        start_hub_str: str = ""
        end_hub_str: str = ""
        hubs_str_list: list[str] = []
        connections_list: list[tuple[str, str]] = []

        # Validate it starts with nb_drones
        for line in lines:
            cleaned_line = line.strip()
            if cleaned_line.startswith("#") or not cleaned_line:
                continue
            if not cleaned_line.startswith("nb_drones:"):
                raise InvalidConfiguration(
                    "[ERROR] Configuration file doesn't start with"
                    " 'nb_drones'.")
            nb_drones_str = cleaned_line.removeprefix("nb_drones:").strip()
            break

        # Extract all tokens
        for line in lines:
            cleaned_line = line.strip()
            if cleaned_line.startswith("#") or not cleaned_line:
                continue

            if cleaned_line.startswith("start_hub:"):
                if start_hub_str:
                    raise InvalidConfiguration(
                        "[ERROR] There are 2 'start_hub' configurations.")
                start_hub_str = cleaned_line.removeprefix("start_hub:").strip()

            elif cleaned_line.startswith("end_hub:"):
                if end_hub_str:
                    raise InvalidConfiguration(
                        "[ERROR] There are 2 'end_hub' configurations.")
                end_hub_str = cleaned_line.removeprefix("end_hub:").strip()

            elif cleaned_line.startswith("hub:"):
                hubs_str_list.append(cleaned_line.removeprefix("hub:").strip())

            elif cleaned_line.startswith("connection:"):
                # Example expected format -> connection: hubA, hubB
                conn_raw = cleaned_line.removeprefix("connection:")
                conn_data = conn_raw.strip().split("-")
                if len(conn_data) == 2:
                    connections_list.append(
                        (conn_data[0].strip(), conn_data[1].strip())
                    )

        # Base Validations
        if not nb_drones_str:
            raise InvalidConfiguration(
                "[ERROR] Missing configuration parameter: 'nb_drones'")
        if not nb_drones_str.isdigit():
            raise InvalidConfiguration(
                f"[ERROR] Invalid configuration parameter: 'nb_drones': "
                f"'{nb_drones_str}'")
        if not start_hub_str:
            raise InvalidConfiguration(
                "[ERROR] Missing configuration parameter: 'start_hub'")
        if not end_hub_str:
            raise InvalidConfiguration(
                "[ERROR] Missing configuration parameter: 'end_hub'")

        # Helper function to convert "name,x,y,[meta1,meta2]"
        # strings into real Hub objects
        def parse_hub_string(hub_str: str) -> Hub:
            cleaned = hub_str.strip()

            bracket_index = cleaned.find("[")
            if bracket_index != -1:
                core_part = cleaned[:bracket_index].strip()
                meta_part = cleaned[bracket_index:].strip("[] ")
                metadata = [t.strip() for t in meta_part.split() if t.strip()]
            else:
                core_part = cleaned
                metadata = None

            parts = core_part.split()
            try:
                if len(parts) < 3:
                    raise ValueError("Missing name or coordinate fields")

                name = parts[0]
                x = int(parts[1])
                y = int(parts[2])

                return Hub(
                    name=name,
                    x_coord=x,
                    y_coord=y,
                    metadata=metadata
                )
            except (IndexError, ValueError) as e:
                raise InvalidConfiguration(
                    f"[ERROR] Failed to parse Hub string: "
                    f"'{hub_str}'. Details: {e}"
                )

        # Turn raw text data into structured Pydantic object instances
        start_hub_obj = parse_hub_string(start_hub_str)
        end_hub_obj = parse_hub_string(end_hub_str)
        hub_objects = [parse_hub_string(h) for h in hubs_str_list]

        return cls(
            nb_drones=int(nb_drones_str),
            start_hub=start_hub_obj,
            end_hub=end_hub_obj,
            hub=hub_objects,
            connection=connections_list
        )
