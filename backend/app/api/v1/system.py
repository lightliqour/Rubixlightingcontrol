from fastapi import APIRouter

from app.config.store import config_store


router = APIRouter()


@router.get("/status")
async def system_status() -> dict[str, str]:
    config = config_store.load()

    return {
        "project": config.project_name,
        "version": config.version,
        "status": "online",
    }