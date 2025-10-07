from __future__ import annotations

from dataclasses import dataclass
from typing import List

from iratc.models.schemas import ScheduleRequest, BlockAssignment


@dataclass
class OptimizationConfig:
    time_limit_ms: int = 500
    max_conflicts: int = 0


class CpsatOptimizer:
    def __init__(self, config: OptimizationConfig | None = None) -> None:
        self.config = config or OptimizationConfig()

    def compute_schedule(self, req: ScheduleRequest) -> List[BlockAssignment]:
        # TODO: implement OR-Tools CP-SAT model; return empty baseline
        return []
