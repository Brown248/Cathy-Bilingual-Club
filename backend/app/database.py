from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# URL สำหรับเชื่อมต่อ Database
# เปลี่ยน username, password, host, port ตามเครื่องคุณ
DATABASE_URL = "postgresql://username:password@localhost/bilingual_club"

# สร้าง engine สำหรับเชื่อมต่อกับ DB
engine = create_engine(DATABASE_URL)

# สร้าง SessionLocal เพื่อใช้สร้าง session กับ DB
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class สำหรับสร้าง ORM models
Base = declarative_base()
