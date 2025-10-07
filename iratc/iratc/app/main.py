from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from iratc.api.v1 import router as api_router

app = FastAPI(title="IRATC API", default_response_class=ORJSONResponse)

app.include_router(api_router, prefix="/api/v1")


@app.get("/healthz")
def health() -> dict[str, str]:
    return {"status": "ok"}
