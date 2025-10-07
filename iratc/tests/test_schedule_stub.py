import pytest
from httpx import AsyncClient, ASGITransport
from iratc.app.main import app
from iratc.ingestion.sample_data import tiny_sample_request


@pytest.mark.asyncio
async def test_schedule_stub():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        req = tiny_sample_request()
        r = await ac.post("/api/v1/schedule", json=req.model_dump())
        assert r.status_code == 200
        body = r.json()
        assert body["feasible"] is True
        assert body["kpis"]["num_trains"] == 2
