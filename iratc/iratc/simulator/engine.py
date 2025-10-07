from __future__ import annotations

from dataclasses import dataclass
from typing import List

from iratc.models.schemas import ScheduleRequest, BlockAssignment


@dataclass
class SimulationConfig:
    horizon_sec: int = 3600


class Simulator:
    def __init__(self, config: SimulationConfig | None = None) -> None:
        self.config = config or SimulationConfig()

    def run(self, req: ScheduleRequest, assignments: List[BlockAssignment]):
        # TODO: implement discrete-event simulation; return zero conflicts baseline
        return {"conflicts": 0}
