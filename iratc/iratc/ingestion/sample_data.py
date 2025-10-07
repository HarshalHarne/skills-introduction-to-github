from __future__ import annotations

from iratc.models.schemas import Block, Station, Train, Network, ScheduleRequest


def tiny_sample_request() -> ScheduleRequest:
    stations = [
        Station(id="S1", name="Alpha", platforms=2),
        Station(id="S2", name="Beta", platforms=2),
    ]
    blocks = [
        Block(id="B1", length_m=2000, max_speed_kmph=80, headway_sec=60),
        Block(id="B2", length_m=2000, max_speed_kmph=80, headway_sec=60),
    ]
    network = Network(
        stations=stations,
        blocks=blocks,
        adjacency={"B1": ["B2"], "B2": []},
    )
    trains = [
        Train(
            id="T1",
            category="EXPRESS",
            origin_station="S1",
            destination_station="S2",
            planned_departure=0,
            planned_arrival=1200,
            priority=7,
        ),
        Train(
            id="T2",
            category="FREIGHT",
            origin_station="S1",
            destination_station="S2",
            planned_departure=120,
            planned_arrival=1500,
            priority=3,
        ),
    ]
    return ScheduleRequest(trains=trains, blocks=blocks, network=network)
