from sqlalchemy.orm import Session
from . import models, schemas

# ดึงนักเรียนทั้งหมด
def get_students(db: Session):
    return db.query(models.Student).all()

# สร้างนักเรียนใหม่
def create_student(db: Session, student: schemas.StudentCreate):
    db_student = models.Student(**student.dict())  # แปลง Pydantic -> ORM
    db.add(db_student)   # เพิ่มเข้า session
    db.commit()          # commit เข้า DB
    db.refresh(db_student) # ดึงข้อมูลล่าสุดกลับ
    return db_student
