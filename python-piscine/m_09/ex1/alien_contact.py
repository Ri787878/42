from datetime import datetime
from pydantic import BaseModel, Field, model_validator, ValidationError
from enum import Enum


class ContactType(Enum):
    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPHATIC = "telephatic"


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime = Field()
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType = Field()
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: str | None = Field(min_length=0, max_length=500)
    is_verified: bool = Field(default=False)

    def __init__(
        self,
        input_contact_id: str,
        input_timestamp: datetime,
        input_location: str,
        input_contact_type: ContactType,
        input_signal_strength: float,
        input_duration_minutes: int,
        input_witness_count: int,
        input_message_received: str | None = None,
        input_is_verified: bool = False,
    ) -> None:
        super().__init__(
            contact_id=input_contact_id,
            timestamp=input_timestamp,
            location=input_location,
            contact_type=input_contact_type,
            signal_strength=input_signal_strength,
            duration_minutes=input_duration_minutes,
            witness_count=input_witness_count,
            message_received=input_message_received,
            is_verified=input_is_verified,
        )

    @model_validator(mode="after")
    def check_input(self) -> "AlienContact":
        if not self.contact_id.startswith("AC"):
            raise ValueError("Contact ID must start with 'AC' (Alien Contact)")
        if self.contact_type == ContactType.PHYSICAL and not self.is_verified:
            raise ValueError("Physical contact reports must be verified")
        if (self.contact_type == ContactType.TELEPHATIC and
           self.witness_count < 3):
            raise ValueError("Telepathic contact "
                             "requires at least 3 witnesses")
        if self.signal_strength > 7.0 and not self.message_received:
            raise ValueError("Strong signals (> 7.0) should include "
                             "received messages")
        return self

    def show_info(self) -> None:
        print(f"ID: {self.contact_id}")
        print(f"Type: {self.contact_type.value}")
        print(f"Location: {self.location}")
        print(f"Signal: {self.signal_strength}/10")
        print(f"Duration: {self.duration_minutes} minutes")
        print(f"Witnesses: {self.witness_count}")
        print(f"Message: {self.message_received}")


def main() -> None:
    valid_contact_id: str = "AC_2024_001"
    valid_timestamp: datetime = datetime.now()
    valid_location: str = "Area 51, Nevada"
    valid_contact_type: ContactType = ContactType.RADIO
    valid_signal_strength: float = 8.5
    valid_duration_minutes: int = 45
    valid_witness_count: int = 5
    valid_message_received: str | None
    valid_message_received = "Greetings from Zeta Reticuli"
    valid_is_verified: bool = True

    invalid_contact_id: str = "AC_2025_002"
    invalid_timestamp: datetime = datetime.now()
    invalid_location: str = "Berlin"
    invalid_contact_type: ContactType = ContactType.TELEPHATIC
    invalid_signal_strength: float = 8.5
    invalid_duration_minutes: int = 30
    invalid_witness_count: int = 2
    invalid_message_received: str | None = None
    invalid_is_verified: bool = False

    try:
        contact_1 = AlienContact(
            valid_contact_id,
            valid_timestamp,
            valid_location,
            valid_contact_type,
            valid_signal_strength,
            valid_duration_minutes,
            valid_witness_count,
            valid_message_received,
            valid_is_verified,
        )
        print("Alien Contact Data Validation")
        print("========================================")
        print("Valid contact created:")
        contact_1.show_info()
        print("\n========================================")

        print("Expected validation error:")

        contact_2 = AlienContact(
            invalid_contact_id,
            invalid_timestamp,
            invalid_location,
            invalid_contact_type,
            invalid_signal_strength,
            invalid_duration_minutes,
            invalid_witness_count,
            invalid_message_received,
            invalid_is_verified,
        )
        contact_2.show_info()
    except ValidationError as e:
        msg = e.errors()[0]["msg"]
        if msg.lower().startswith("value error, "):
            msg = msg.split(", ", 1)[1]
            print(msg)


if __name__ == "__main__":
    main()
