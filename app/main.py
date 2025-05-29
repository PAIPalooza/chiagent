from fastapi import FastAPI
from app.api.api_v1.api import router
from app.core.config import settings

app = FastAPI(
    title="chiagent",
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

app.include_router(router, prefix=settings.API_V1_STR)
