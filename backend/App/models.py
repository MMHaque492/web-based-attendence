from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.sql import func
from .db import Base


class User(Base):
__tablename__ = "users"
id = Column(Integer, primary_key=True, index=True)
email = Column(String, unique=True, index=True)
name = Column(String)
role = Column(String, default="student")
device_id = Column(String, nullable=True)
face_embedding = Column(String, nullable=True) # placeholder to store embedding reference


class Session(Base):
__tablename__ = "sessions"
id = Column(Integer, primary_key=True, index=True)
teacher_id = Column(Integer)
course = Column(String)
started_at = Column(DateTime(timezone=True), server_default=func.now())
qr_token = Column(String)


class Attendance(Base):
__tablename__ = "attendance"
id = Column(Integer, primary_key=True, index=True)
session_id = Column(Integer, ForeignKey("sessions.id"))
student_id = Column(Integer, ForeignKey("users.id"))
timestamp = Column(DateTime(timezone=True), server_default=func.now())
method = Column(String) # qr+geo+face
status = Column(String)