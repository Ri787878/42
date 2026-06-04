from datetime import datetime
from pydantic import BaseModel, Field, ValidationError


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime = Field()
    is_operational: bool = Field(default=True)
    notes: str | None = Field(min_length=0, max_length=200)

    def __init__(
        self,
        input_id: str,
        input_name: str,
        input_size: int,
        input_power: float, input_oxygen: float,
        input_maintenance: datetime,
        input_operacional_status: bool,
        input_notes: str | None
    ) -> None:
        super().__init__(
            station_id=input_id,
            name=input_name,
            crew_size=input_size,
            power_level=input_power,
            oxygen_level=input_oxygen,
            last_maintenance=input_maintenance,
            is_operational=input_operacional_status,
            notes=input_notes,
        )

    def print_info(self) -> None:
        print(f"ID: {self.station_id}")
        print(f"Name: {self.name}")
        print(f"Crew: {self.crew_size} people")
        print(f"Power: {self.power_level}%")
        print(f"Oxygen: {self.oxygen_level}%")
        if self.is_operational:
            print("Status: Operational")
        else:
            print("Status: Not Operational")


def main() -> None:
    station_1_id: str = "ISS001"
    station_1_name: str = "International Space Station"
    station_1_crew_size: int = 6
    station_1_power_level: float = 85.5
    station_1_oxygen_level: float = 92.3
    station_1_last_maintenance: datetime = datetime.now()
    station_1_is_operational: bool = True
    station_1_notes: str | None = None

    station_2_id: str = "ISS002"
    station_2_name: str = "Lunar Gateway"
    station_2_crew_size: int = 25
    station_2_power_level: float = 78.0
    station_2_oxygen_level: float = 90.1
    station_2_last_maintenance: datetime = datetime.now()
    station_2_is_operational: bool = False
    station_2_notes: str | None = "Needs inspection"

    try:
        station_1 = SpaceStation(
            station_1_id,
            station_1_name,
            station_1_crew_size,
            station_1_power_level,
            station_1_oxygen_level,
            station_1_last_maintenance,
            station_1_is_operational,
            station_1_notes,
        )

        print("Space Station Data Validation")
        print("========================================")
        print("Valid station created:")
        station_1.print_info()
        print("\n========================================")

        print("Expected validation error:")

        station_2 = SpaceStation(
            station_2_id,
            station_2_name,
            station_2_crew_size,
            station_2_power_level,
            station_2_oxygen_level,
            station_2_last_maintenance,
            station_2_is_operational,
            station_2_notes,
        )
        station_2.print_info()
    except ValidationError as e:
        print(e.errors()[0]["msg"])


if __name__ == "__main__":
    main()
