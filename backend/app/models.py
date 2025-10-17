from sqlalchemy import Column, Integer, String, ForeignKey, TIMESTAMP
from .database import Base
from datetime import datetime

# Model นักเรียน
class Student(Base):
    __tablename__ = "students"  # ชื่อตารางใน DB
    id = Column(Integer, primary_key=True, index=True)  # primary key + index
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String, unique=True, index=True)  # ต้องไม่ซ้ำ
    phone = Column(String)
    created_at = Column(TIMESTAMP, default=datetime.utcnow)  # สร้างเวลาอัตโนมัติ

# Model ครู
class Teacher(Base):
    __tablename__ = "teachers"
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String, unique=True, index=True)
    phone = Column(String)
    created_at = Column(TIMESTAMP, default=datetime.utcnow)
