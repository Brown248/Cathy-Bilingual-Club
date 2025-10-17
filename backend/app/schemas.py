from pydantic import BaseModel

# Schema พื้นฐานของนักเรียน
class StudentBase(BaseModel):
    first_name: str
    last_name: str
    email: str
    phone: str

# Schema สำหรับสร้างนักเรียนใหม่
class StudentCreate(StudentBase):
    pass

# Schema สำหรับ response (รวม id)
class Student(StudentBase):
    id: int
    class Config:
        orm_mode = True  # บอก Pydantic ให้แปลงจาก ORM Model เป็น dict
