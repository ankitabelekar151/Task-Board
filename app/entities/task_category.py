from pydantic import BaseModel, Field

class TaskCategoryEntity(BaseModel):
    task_id: str
    category_id: str
