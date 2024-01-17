from pydantic import BaseModel
from datetime import date
from datetime import datetime


class TaskCreate(BaseModel):
    title: str
    description: str 
    created_at: date = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
    completed_at: bool = False
    updated_at: date = None
