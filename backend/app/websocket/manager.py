from fastapi import WebSocket


class WebSocketManager:
    def __init__(self) -> None:
        self.connections: set[WebSocket] = set()

    async def connect(self, websocket: WebSocket) -> None:
        await websocket.accept()
        self.connections.add(websocket)

    def disconnect(self, websocket: WebSocket) -> None:
        self.connections.discard(websocket)

    async def broadcast(self, message: str) -> None:
        for websocket in tuple(self.connections):
            try:
                await websocket.send_text(message)
            except Exception:
                self.disconnect(websocket)


websocket_manager = WebSocketManager()