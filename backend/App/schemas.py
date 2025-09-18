from pydantic import BaseModel
from typing import Optional


class UserCreate(BaseModel):
email: str
name: str
role: Optional[str] = "student"


class UserOut(BaseModel):
id: int
email: str
name: str
role: str


class Config:
orm_mode = True