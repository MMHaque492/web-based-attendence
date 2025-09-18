from fastapi import APIRouter, File, UploadFile


router = APIRouter()


@router.post("/verify")
async def verify_face(file: UploadFile = File(...), student_id: int = 0):
# PLACEHOLDER: run face verification against stored embedding.
# For prototype we always return success. Replace with real model call.
content = await file.read()
return {"status": "ok", "match": True, "confidence": 0.98}