# IRATC Backend

FastAPI backend for Indian Railway Automated Traffic Control (IRATC).

## Quickstart

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .[dev]
uvicorn iratc.app.main:app --reload
```

## Structure
- `app/` FastAPI app wiring
- `api/` route handlers
- `models/` pydantic and domain types
- `optimizer/` OR-Tools integration
- `simulator/` discrete-event simulation
- `ingestion/` parsers and adapters
- `tests/` unit tests
