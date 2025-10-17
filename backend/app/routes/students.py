from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import crud, models, schemas
from ..database import SessionLocal

router = APIRouter(prefix="/students", tags=["students"])

# Dependency สำหรับดึง session DB
def get_db():
    db = SessionLocal()  # สร้าง session
    try:
        yield db          # ใช้งานใน route
    finally:
        db.close()        # ปิด session หลังใช้เสร็จ

# Route GET /students/
@router.get("/")
def read_students(db: Session = Depends(get_db)):
    return crud.get_students(db)
