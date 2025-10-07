import pytest
from httpx import AsyncClient, ASGITransport
from iratc.app.main import app
from iratc.ingestion.sample_data import tiny_sample_request


@pytest.mark.asyncio
async def test_simulate_stub():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        req = tiny_sample_request()
        r = await ac.post("/api/v1/simulate", json={"request": req.model_dump(), "assignments": []})
        assert r.status_code == 200
        body = r.json()
        assert body["conflicts"] == 0


@pytest.mark.asyncio
async def test_what_if_stub():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        req = tiny_sample_request()
        r = await ac.post("/api/v1/what_if", json={"request": req.model_dump(), "additional_disturbances": []})
        assert r.status_code == 200


@pytest.mark.asyncio
async def test_reoptimize_stub():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        req = tiny_sample_request()
        r = await ac.post("/api/v1/reoptimize", json={"request": req.model_dump(), "locked_assignments": []})
        assert r.status_code == 200
        assert r.json()["feasible"] is True
