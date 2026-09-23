from contextlib import asynccontextmanager
import logging

from fastapi import FastAPI

from app.api.v1.router import router as api_v1_router
from app.config.store import config_store
from app.core.logging import configure_logging


logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    config = config_store.load()

    configure_logging()

    app.state.config = config

    logger.info(
        "Starting %s %s",
        config.project_name,
        config.version,
    )

    yield

    logger.info(
        "Stopping %s",
        config.project_name,
    )


initial_config = config_store.load()

app = FastAPI(
    title=initial_config.project_name,
    version=initial_config.version,
    lifespan=lifespan,
)

app.include_router(
    api_v1_router,
    prefix="/api/v1",
)


@app.get("/")
async def root() -> dict[str, str]:
    config = config_store.load()

    return {
        "project": config.project_name,
        "version": config.version,
        "status": "online",
    }