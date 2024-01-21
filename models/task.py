from sqlalchemy import Column, String, Date, Boolean, Integer
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Task(Base):
    __tablename__ = "tasks"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String)
    description = Column(String)
    created_at = Column(Date)
    completed_at = Column(Boolean)
    updated_at = Column(Date)