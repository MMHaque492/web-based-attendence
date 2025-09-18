# backend/app/routes/attendance.py
from fastapi import APIRouter, Request
from pydantic import BaseModel

router = APIRouter()

class AttendanceMark(BaseModel):
    session_id: int
    student_id: int
    qr_token: str
    latitude: float
    longitude: float

@router.post("/mark")
async def mark(request: Request, att: AttendanceMark):
    # PLACEHOLDER: real validation (QR, geofence, face verification) should go here
    if not att.qr_token:
        return {"status": "error", "reason": "invalid qr"}

    # pretend we recorded attendance and create a payload
    payload = {
        "status": "ok",
        "detail": "attendance recorded (stub)",
        "session_id": att.session_id,
        "student_id": att.student_id,
        "timestamp": None,   # you can fill server time if desired
        "method": "qr+geo+face",
    }

    # Broadcast to all websocket clients connected to the session
    manager = request.app.state.manager
    try:
        await manager.broadcast(str(att.session_id), {"type": "attendance_marked", "data": payload})
    except Exception:
        # fail silently for prototype
        pass

    return payload
