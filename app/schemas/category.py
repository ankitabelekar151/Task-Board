from pydantic import BaseModel, Field
from typing import Optional

class CategoryCreateSchema(BaseModel):
    name: str
    description: str

class CategoryResponseSchema(BaseModel):
    id: str = Field(..., alias="_id")
    name: str
    description: str

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
