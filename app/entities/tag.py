from typing import Optional
from pydantic import BaseModel, Field

class TagEntity(BaseModel):
    id: Optional[str] = Field(None, alias="_id")
    name: str
