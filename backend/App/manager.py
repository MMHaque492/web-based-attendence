# backend/app/manager.py
from typing import Dict, List
from fastapi import WebSocket
import asyncio

class ConnectionManager:
    def __init__(self):
        # map session_id (int/str) -> list of websockets
        self.active_connections: Dict[str, List[WebSocket]] = {}

    async def connect(self, session_id: str, websocket: WebSocket):
        await websocket.accept()
        conns = self.active_connections.get(session_id, [])
        conns.append(websocket)
        self.active_connections[session_id] = conns

    def disconnect(self, session_id: str, websocket: WebSocket):
        conns = self.active_connections.get(session_id, [])
        if websocket in conns:
            conns.remove(websocket)
        if conns:
            self.active_connections[session_id] = conns
        else:
            self.active_connections.pop(session_id, None)

    async def send_personal_message(self, websocket: WebSocket, message):
        await websocket.send_json(message)

    async def broadcast(self, session_id: str, message):
        conns = list(self.active_connections.get(session_id, []))
        for connection in conns:
            try:
                await connection.send_json(message)
            except Exception:
                # best-effort: ignore broken connections
                try:
                    self.disconnect(session_id, connection)
                except Exception:
                    pass
