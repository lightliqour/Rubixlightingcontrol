from fastapi import APIRouter

from app.config.models import ControllerConfig
from app.config.store import config_store


router = APIRouter()


@router.get("/")
async def get_settings() -> dict[str, object]:
    return config_store.load().to_dict()


@router.put("/")
async def update_settings(
    config: ControllerConfig,
) -> dict[str, object]:
    config_store.save(config)
    return config.to_dict()