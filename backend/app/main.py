from contextlib import asynccontextmanager
import logging

from fastapi import FastAPI

from app.api.v1.router import router as api_v1_router
from app.core.config import settings
from app.core.logging import configure_logging


logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    configure_logging()

    logger.info(
        "Starting %s %s",
        settings.project_name,
        settings.version,
    )

    yield

    logger.info(
        "Stopping %s",
        settings.project_name,
    )


app = FastAPI(
    title=settings.project_name,
    version=settings.version,
    lifespan=lifespan,
)


app.include_router(
    api_v1_router,
    prefix="/api/v1",
)


@app.get("/")
async def root() -> dict[str, str]:
    return {
        "project": settings.project_name,
        "version": settings.version,
        "status": "online",
    }