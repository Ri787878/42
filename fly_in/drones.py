from zone_network import Zone_Network, Hub
from variables import DroneStatus
from pydantic import BaseModel, Field


class Drone(BaseModel):
    """Represents one drone moving through the network."""

    current_hub: Hub
    planned_path: list[Hub] = Field(default_factory=list)
    next_step_index: int = Field(default=0, ge=0)
    status: DroneStatus = Field(default=DroneStatus.IDLE)

    def next_hub(self) -> Hub | None:
        if self.next_step_index >= len(self.planned_path):
            return None
        return self.planned_path[self.next_step_index]

    def has_arrived(self) -> bool:
        return self.status == DroneStatus.ARRIVED

    def advance(self) -> None:
        if self.next_step_index < len(self.planned_path):
            self.current_hub = self.planned_path[self.next_step_index]
            self.next_step_index += 1

        if self.next_step_index >= len(self.planned_path):
            self.status = DroneStatus.ARRIVED
        else:
            self.status = DroneStatus.MOVING

    @staticmethod
    def build_drone(network: Zone_Network, route: list[Hub]) -> "Drone":
        return Drone(
            current_hub=network.start_hub,
            planned_path=route,
            next_step_index=1,
            status=(
                DroneStatus.MOVING
                if len(route) > 1
                else DroneStatus.ARRIVED
            ),
        )
