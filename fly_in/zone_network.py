from pydantic import BaseModel, Field, model_validator
from enum import Enum
# , ValidationError


class Tags(Enum):
    """Available tags for a hub."""
    NORMAL = "normal"
    BLOCKED = "blocked",
    RESTRICTED = "restricted",
    PRIORITY = "priority"


class Hub(BaseModel):
    # Base Values
    name: str = Field(min_length=1)
    x_coord: int = Field(ge=0)
    y_coord: int = Field(ge=0)
    movement_cost: int = Field(default=1)
    is_blocked: bool = Field(default=False)
    prefered_zone: bool = Field(default=False)

    # Metadata
    zone: str = Field(default="normal")
    color: str = Field(default="white")
    max_drones: int = Field(default=1)
    metadata: list[str] | None = None

    @model_validator(mode="after")
    def validate_hub(self) -> "Hub":
        # Check Errors in Inputed values
        if "-" in self.name or " " in self.name:
            raise ValueError(
                f"[ERROR] Hub {self.name} can't have ' ' or '-'.")
        if " " in self.color:
            raise ValueError(
                f"[ERROR] Hub {self.name} can't have multi word colors"
                f" '{self.color}'.")

        if (self.x_coord < 0) or (self.y_coord < 0):
            raise ValueError(
                f"[ERROR] Hub {self.name} coordenates are invalid"
                f" ({self.x_coord},{self.y_coord}).")

        # Apply configurations depending on existing Metadata
        self.apply_metadata()
        self.apply_zone_qualifiers()

        return self

    def apply_metadata(self) -> None:
        if not self.metadata:
            return
        else:
            for metadata in self.metadata:
                if "zone" in metadata:
                    self.zone = metadata[5:]
                if "color" in metadata:
                    self.zone = metadata[6:]
                if "max_drones" in metadata:
                    self.zone = metadata[10:]

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
    hub: list[Hub]
    connection: list[tuple[str, str]] = Field()

    @model_validator(mode="after")
    def check_inputs(self) -> "Zone_Network":
        # TODO: add a check for unique start and end zone coordenates
        return self
