from datetime import datetime
from pydantic import BaseModel, Field
from typing import Optional, List

class TaskCreateSchema(BaseModel):
    title: str
    description: str
    due_date: datetime
    category_ids: Optional[List[str]] = []
    tag_ids: Optional[List[str]] = []

class TaskUpdateStatusSchema(BaseModel):
    status: str

class TaskResponseSchema(BaseModel):
    id: str = Field(..., alias="_id")
    title: str
    description: str
    due_date: datetime
    status: str
    deleted: bool
    category_ids: Optional[List[str]] = []
    tag_ids: Optional[List[str]] = []

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
