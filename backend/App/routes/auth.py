from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from app.db import SessionLocal, engine
from app import models


models.Base.metadata.create_all(bind=engine)


router = APIRouter()


class LoginData(BaseModel):
email: str
device_id: str = None


@router.post("/login")
async def login(data: LoginData):
# PLACEHOLDER: implement real auth, JWT issuance.
# For prototype, we return a fake token and user role.
if data.email.endswith("@example.com"):
return {"access_token": "fake-token", "token_type": "bearer", "user": {"email": data.email, "role": "student"}}
return {"access_token": "fake-token-teacher", "token_type": "bearer", "user": {"email": data.email, "role": "teacher"}}


@router.post("/register")
async def register(payload: dict):
# PLACEHOLDER: save user to DB
return {"status": "ok", "message": "user registered (stub)"}