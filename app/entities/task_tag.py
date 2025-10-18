from pydantic import BaseModel, Field

class TaskTagEntity(BaseModel):
    task_id: str
    tag_id: str
