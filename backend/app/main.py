from fastapi import FastAPI
from app.routes import students
from app.database import Base, engine

# สร้างตารางใน DB ถ้ายังไม่มี
Base.metadata.create_all(bind=engine)

# สร้าง FastAPI app
app = FastAPI()

# รวม route ของนักเรียน
app.include_router(students.router)
