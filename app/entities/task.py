from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel, Field

class TaskEntity(BaseModel):
    id: Optional[str] = Field(None, alias="_id")
    title: str
    description: str
    due_date: datetime
    status: str = "pending"
    deleted: bool = False
    category_ids: Optional[List[str]] = Field(default_factory=list)
    tag_ids: Optional[List[str]] = Field(default_factory=list)

    class Config:
        populate_by_name = True
        from_attributes = True
