from fastapi import APIRouter
from pydantic import BaseModel
import uuid


router = APIRouter()


class SessionCreate(BaseModel):
teacher_id: int
course: str


@router.post("/create")
async def create_session(payload: SessionCreate):
# PLACEHOLDER: persist session and generate QR token
token = str(uuid.uuid4())
return {"session_id": 1, "qr_token": token, "qr_url": f"https://example.com/qr/{token}"}


@router.get("/active/{session_id}")
async def active(session_id: int):
# PLACEHOLDER: return fake active session
return {"session_id": session_id, "started_at": "now", "course": "Demo Course"}