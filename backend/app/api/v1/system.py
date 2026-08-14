from fastapi import APIRouter

from app.core.config import settings


router = APIRouter()


@router.get("/status")
async def system_status() -> dict[str, str]:
    return {
        "project": settings.project_name,
        "version": settings.version,
        "status": "online",
    }