from pydantic import BaseModel, Field, model_validator
from zone_network import InvalidConfiguration
from variables import Approved_tags


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
