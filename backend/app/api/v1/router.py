from fastapi import APIRouter, WebSocket

from app.api.v1.settings import router as settings_router
from app.api.v1.system import router as system_router
from app.websocket.manager import websocket_manager


router = APIRouter()

router.include_router(
    system_router,
    prefix="/system",
    tags=["system"],
)

router.include_router(
    settings_router,
    prefix="/settings",
    tags=["settings"],
)


@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket) -> None:
    await websocket_manager.connect(websocket)

    try:
        while True:
            message = await websocket.receive_text()
            await websocket_manager.broadcast(message)
    except Exception:
        websocket_manager.disconnect(websocket)