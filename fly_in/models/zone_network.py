from pydantic import BaseModel, Field, model_validator
from .error_handling import InvalidConfiguration
from typing_extensions import Self
from pathlib import Path
from models.hub import Hub


class Zone_Network(BaseModel):
    nb_drones: int = Field(ge=1)
    start_hub: Hub
    end_hub: Hub
    hubs: list[Hub] = Field(default_factory=list)
    connection: list[tuple[str, str, int]] = Field(default_factory=list)
    hub_map: dict[str, Hub] = Field(default_factory=dict, exclude=True)
    adjacency: dict[str, list[Hub]] = Field(default_factory=dict, exclude=True)
    connection_lines: list[int] = Field(default_factory=list, exclude=True)

    @model_validator(mode="after")
    def check_inputs(self) -> "Zone_Network":
        # Check if start and end hubs are in the exact same spot
        if (self.start_hub.x_coord == self.end_hub.x_coord and
                self.start_hub.y_coord == self.end_hub.y_coord):
            raise ValueError(
                "[ERROR] Start hub and End hub cannot"
                " share the same coordinates.")
        if (self.start_hub.name == self.end_hub.name):
            raise ValueError(
                f"[ERROR] [Line {self.start_hub.line_index}] Start hub "
                f"and End Hub can't have the same name."
            )
        hub_names = [hub.name for hub in self.hubs]
        for hub in self.hubs:
            if self.start_hub.name == hub.name:
             raise ValueError(
                f"[ERROR] [Line {self.start_hub.line_index}] Start hub "
                f"and Hub {hub.name} can't have the same name."
            )
            if self.end_hub.name == hub.name:
             raise ValueError(
                f"[ERROR] [Line {self.end_hub.line_index}] End hub "
                f"and Hub {hub.name} can't have the same name."
            )

            if hub_names.count(hub.name) > 1:
                raise ValueError(
                    f"[ERROR] [Line {hub.line_index}] End hub "
                    f"and Hub {hub.name} can't have the same name."
                )

        self.end_hub.max_drones = self.nb_drones

        self.hub_map = self.build_hub_map()
        known_hub_names = set(self.hub_map)
        seen_connections: set[frozenset[str]] = set()
        for connection_index, (left_name, right_name, _cap) in enumerate(
                self.connection):
            line_number = (
                self.connection_lines[connection_index]
                if connection_index < len(self.connection_lines)
                else 0
            )
            unknown_names = {
                name for name in (left_name, right_name)
                if name not in known_hub_names
            }
            if unknown_names:
                raise ValueError(
                    f"[ERROR] [Line {line_number}] Connection references "
                    "unknown hub(s): "
                    f"{', '.join(sorted(unknown_names))}."
                )
            connection_key = frozenset((left_name, right_name))
            if connection_key in seen_connections:
                raise ValueError(
                    f"[ERROR] [Line {line_number}] Duplicate connection: "
                    f"{left_name}-{right_name}."
                )
            seen_connections.add(connection_key)
        self.adjacency = self.build_adjacency()

        return self

    def build_hub_map(self) -> dict[str, Hub]:
        hubs = [self.start_hub, self.end_hub, *self.hubs]
        return {hub.name: hub for hub in hubs}

    def build_adjacency(self) -> dict[str, list[Hub]]:
        adjacency: dict[str, list[Hub]] = {
            name: [] for name in self.build_hub_map()}

        for left_name, right_name, _cap in self.connection:
            left_hub = self.hub_map[left_name]
            right_hub = self.hub_map[right_name]
            adjacency[left_name].append(right_hub)
            adjacency[right_name].append(left_hub)

        return adjacency

    def neighbors(self, hub_name: str) -> list[Hub]:
        return self.adjacency.get(hub_name, [])

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
        hubs_index_list: list[int] = []
        connections_list: list[tuple[str, str, int]] = []
        connection_lines: list[int] = []
        current_hub_name: str = ""
        i: int = 0
        nb_drones_line: int = 0
        end_hub_line: int = 0

        # Validate it starts with nb_drones
        for line in lines:
            i += 1
            cleaned_line = line.strip()
            if cleaned_line.startswith("#") or not cleaned_line:
                continue
            if not cleaned_line.startswith("nb_drones:"):
                raise InvalidConfiguration(
                    f"[ERROR] [Line {i}] Configuration file doesn't start with"
                    f" 'nb_drones'.")
            nb_drones_str = cleaned_line.removeprefix("nb_drones:").strip()
            nb_drones_line = i
            break

        i = 0
        # Extract all tokens
        for line in lines:
            i += 1
            cleaned_line = line.strip()
            if cleaned_line.startswith("#") or not cleaned_line:
                continue

            if cleaned_line.startswith("start_hub:"):
                if start_hub_str:
                    raise InvalidConfiguration(
                        f"[ERROR] [Line {i}] There are 2 'start_hub' "
                        f"configurations."
                    )
                start_hub_str = cleaned_line.removeprefix("start_hub:").strip()
                start_line: int = i

            elif cleaned_line.startswith("end_hub:"):
                if end_hub_str:
                    raise InvalidConfiguration(
                        f"[ERROR] [Line {i}] There are 2 'end_hub' "
                        f"configurations."
                    )
                end_hub_str = cleaned_line.removeprefix("end_hub:").strip()
                end_line: int = i

            elif cleaned_line.startswith("hub:"):
                current_hub_name = cleaned_line.removeprefix("hub:").strip()
                
                hubs_str_list.append(current_hub_name)
                hubs_index_list.append(i)

            elif cleaned_line.startswith("connection:"):
                raw = cleaned_line.removeprefix("connection:").strip()

                bracket_i = raw.find("[")
                if bracket_i != -1:
                    core = raw[:bracket_i].strip()
                    meta_tokens = [
                        t.strip()
                        for t in raw[bracket_i:].strip("[] ").split()
                        if t.strip()
                    ]
                else:
                    core = raw
                    meta_tokens = []

                conn_data = core.split("-")
                if (len(conn_data) != 2 or
                        not conn_data[0].strip() or
                        not conn_data[1].strip()):
                    raise InvalidConfiguration(
                        f"[ERROR] [Line {i}] Invalid connection: '{raw}'."
                    )

                left_name = conn_data[0].strip()
                right_name = conn_data[1].strip()

                cap = 1  # default
                for tok in meta_tokens:
                    if tok.startswith("max_link_capacity="):
                        cap = int(tok.split("=", 1)[1].strip())

                connections_list.append((left_name, right_name, cap))
                connection_lines.append(i)

        # Base Validations
        if not nb_drones_str:
            raise InvalidConfiguration(
                "[ERROR] Missing configuration parameter: 'nb_drones'")
        if not nb_drones_str.isdigit():
            raise InvalidConfiguration(
                f"[ERROR] [{nb_drones_line}] Invalid configuration "
                f"parameter: 'nb_drones': '{nb_drones_str}'"
            )
        if not start_hub_str:
            raise InvalidConfiguration(
                "[ERROR] Missing configuration parameter: 'start_hub'")
        if not end_hub_str:
            raise InvalidConfiguration(
                f"[ERROR] [{end_hub_line}] Missing configuration"
                f" parameter: 'end_hub'"
            )

        # Helper function to convert "name,x,y,[meta1,meta2]"
        # strings into real Hub objects
        def parse_hub_string(hub_str: str, line_index: int) -> Hub:
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
                    metadata=metadata,
                    line_index=line_index
                )
            except (IndexError, ValueError) as e:
                raise InvalidConfiguration(
                    f"[ERROR] Failed to parse Hub string: "
                    f"'{hub_str}'. Details: {e}"
                )

        # Turn raw text data into structured Pydantic object instances
        start_hub_obj = parse_hub_string(start_hub_str, start_line)
        end_hub_obj = parse_hub_string(end_hub_str, end_line)
        end_hub_obj.max_drones = int(nb_drones_str)
        hub_objects = [
            parse_hub_string(
                h,
                hubs_index_list[hubs_str_list.index(h)]
            ) for h in hubs_str_list]

        return cls(
            nb_drones=int(nb_drones_str),
            start_hub=start_hub_obj,
            end_hub=end_hub_obj,
            hubs=hub_objects,
            connection=connections_list,
            connection_lines=connection_lines
        )
