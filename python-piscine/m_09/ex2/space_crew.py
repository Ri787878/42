from datetime import datetime
from pydantic import BaseModel, Field, model_validator, ValidationError
from enum import Enum


class ContactType(Enum):
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTIAN = "captian"
    COMMANDER = "COMMANDER"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: ContactType = Field()
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = Field(default=True)

    def __init__(
        self,
        input_member_id: str,
        input_name: str,
        input_rank: ContactType,
        input_age: int,
        input_specialization: str,
        input_years_experience: int,
        input_is_active: bool = True,
    ) -> None:
        super().__init__(
            member_id=input_member_id,
            name=input_name,
            rank=input_rank,
            age=input_age,
            specialization=input_specialization,
            years_experience=input_years_experience,
            is_active=input_is_active,
        )


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime = Field()
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(ge=1.0, le=10000.0)

    def __init__(
        self,
        input_mission_id: str,
        input_mission_name: str,
        input_destination: str,
        input_launch_date: datetime,
        input_duration_days: int,
        input_crew: list[CrewMember],
        input_mission_status: str = "planned",
        input_budget_millions: float = 1.0,
    ) -> None:
        super().__init__(
            mission_id=input_mission_id,
            mission_name=input_mission_name,
            destination=input_destination,
            launch_date=input_launch_date,
            duration_days=input_duration_days,
            crew=input_crew,
            mission_status=input_mission_status,
            budget_millions=input_budget_millions,
        )

    def show_stats(self) -> None:
        print(f"Mission: {self.mission_name}")
        print(f"ID: {self.mission_id}")
        print(f"Destination: {self.destination}")
        print(f"Duration: {self.duration_days} days")
        print(f"Budget: ${self.budget_millions}M")
        print(f"Crew size: {len(self.crew)}")
        print("Crew members:")
        for member in self.crew:
            print(f"- {member.name} ({member.rank.value.lower()})"
                  f" - {member.specialization}")

    @model_validator(mode="after")
    def check_input(self) -> "SpaceMission":
        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID must start with 'M'")

        if not exists_leader(self.crew):
            raise ValueError("Mission must have at least "
                             "one Commander or Captain")

        if not are_all_experienced(self.crew):
            raise ValueError("Long missions (> 365 days) need "
                             "50% experienced crew (5+ years)")

        if not are_all_active(self.crew):
            raise ValueError("All crew members must be active")
        return self


def are_all_active(crew: list[CrewMember]) -> bool:
    for member in crew:
        if not member.is_active:
            return False
    return True


def are_all_experienced(crew: list[CrewMember]) -> bool:
    crew_size: int = len(crew)
    experienced_crew_counter: int = 0
    for member in crew:
        if member.years_experience >= 5:
            experienced_crew_counter += 1
    if experienced_crew_counter >= (crew_size / 2):
        return True
    else:
        return False


def exists_leader(crew: list[CrewMember]) -> bool:
    for member in crew:
        if (member.rank == ContactType.COMMANDER
           or member.rank == ContactType.CAPTIAN):
            return True
    return False


def main() -> None:
    valid_crew = [
        CrewMember(
            "CM001",
            "Sarah Connor",
            ContactType.COMMANDER,
            38,
            "Mission Command",
            12,
            True,
        ),
        CrewMember(
            "CM002",
            "John Smith",
            ContactType.LIEUTENANT,
            32,
            "Navigation",
            8,
            True,
        ),
        CrewMember(
            "CM003",
            "Alice Johnson",
            ContactType.OFFICER,
            29,
            "Engineering",
            6,
            True,
        ),
    ]

    invalid_crew = [
        CrewMember(
            "CM003",
            "Eve",
            ContactType.CADET,
            19,
            "Research",
            1,
            False,
        ),
        CrewMember(
            "CM004",
            "Mallory",
            ContactType.LIEUTENANT,
            22,
            "Science",
            2,
            False,
        ),
    ]

    mission_1 = SpaceMission(
        "M2024_MARS",
        "Mars Colony Establishment",
        "Mars",
        datetime.now(),
        900,
        valid_crew,
        "planned",
        2500.0,
    )

    print("Space Mission Data Validation")
    print("========================================")
    print("Valid mission created:")
    mission_1.show_stats()
    print("\n========================================")
    print("Expected validation error:")

    try:
        mission_2 = SpaceMission(
            "M2024_MARS",
            "Mars Colony Establishment",
            "Mars",
            datetime.now(),
            900,
            invalid_crew,
            "planned",
            2500.0,
        )
        mission_2.show_stats()
    except ValidationError as e:
        msg = e.errors()[0]["msg"]
        if msg.lower().startswith("value error, "):
            msg = msg.split(", ", 1)[1]
        print(msg)


if __name__ == "__main__":
    main()
