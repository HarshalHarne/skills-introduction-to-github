from __future__ import annotations

from typing import Literal, Optional

from pydantic import BaseModel, Field


class Block(BaseModel):
    id: str
    length_m: float
    max_speed_kmph: float
    headway_sec: int = 60
    direction: Literal["UP", "DOWN", "BIDIR"] = "BIDIR"


class Station(BaseModel):
    id: str
    name: str
    platforms: int = 1


class Train(BaseModel):
    id: str
    category: Literal["EXPRESS", "SUBURBAN", "FREIGHT", "SPECIAL", "MAINTENANCE"]
    origin_station: str
    destination_station: str
    planned_departure: int  # epoch seconds
    planned_arrival: int  # epoch seconds
    priority: int = Field(ge=1, le=10, default=5)
    max_speed_kmph: Optional[float] = None


class Network(BaseModel):
    stations: list[Station]
    blocks: list[Block]
    adjacency: dict[str, list[str]]  # block -> next block ids


class Disturbance(BaseModel):
    type: Literal["DELAY", "BLOCK_DOWN", "WEATHER", "BREAKDOWN"]
    target_id: str
    delay_sec: Optional[int] = None


class ScheduleRequest(BaseModel):
    trains: list[Train]
    blocks: list[Block]
    network: Network
    disturbances: list[Disturbance] = []


class RunConfig(BaseModel):
    time_limit_ms: int = 500
    objective: Literal["lateness", "makespan", "weighted_lateness"] = "lateness"
    horizon_sec: int = 4 * 3600


class BlockAssignment(BaseModel):
    train_id: str
    block_id: str
    enter_time: int
    exit_time: int


class ScheduleResponse(BaseModel):
    feasible: bool
    message: str
    assignments: list[BlockAssignment]
    kpis: dict[str, float]


class SimulateRequest(BaseModel):
    request: ScheduleRequest
    assignments: list[BlockAssignment]


class WhatIfRequest(BaseModel):
    request: ScheduleRequest
    additional_disturbances: list[Disturbance] = []


class ReoptimizeRequest(BaseModel):
    request: ScheduleRequest
    locked_assignments: list[BlockAssignment] = []
