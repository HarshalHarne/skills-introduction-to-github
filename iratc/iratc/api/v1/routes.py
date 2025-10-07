from fastapi import APIRouter

from iratc.models.schemas import (
    ScheduleRequest,
    ScheduleResponse,
    SimulateRequest,
    WhatIfRequest,
    ReoptimizeRequest,
)

router = APIRouter()


@router.post("/schedule", response_model=ScheduleResponse)
def schedule(req: ScheduleRequest) -> ScheduleResponse:
    # Placeholder: echo back number of trains and blocks
    return ScheduleResponse(
        feasible=True,
        message="stub",
        assignments=[],
        kpis={
            "num_trains": len(req.trains),
            "num_blocks": len(req.blocks),
        },
    )


@router.post("/simulate")
def simulate(_: SimulateRequest) -> dict:
    return {"conflicts": 0, "message": "stub"}


@router.post("/what_if")
def what_if(_: WhatIfRequest) -> dict:
    return {"result": "stub"}


@router.post("/reoptimize")
def reoptimize(_: ReoptimizeRequest) -> ScheduleResponse:
    return ScheduleResponse(feasible=True, message="stub", assignments=[], kpis={})
