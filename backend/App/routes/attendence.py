from fastapi import APIRouter, File, UploadFile, Form
from pydantic import BaseModel


router = APIRouter()


class AttendanceMark(BaseModel):
session_id: int
student_id: int
qr_token: str
latitude: float
longitude: float


@router.post("/mark")
async def mark(att: AttendanceMark):
# PLACEHOLDER: validate QR token, geofence, face verification
# For prototype: simple rule: if qr_token is non-empty => accepted
if not att.qr_token:
return {"status": "error", "reason": "invalid qr"}
return {"status": "ok", "detail": "attendance recorded (stub)", "session_id": att.session_id, "student_id": att.student_id}
