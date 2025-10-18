from app.db import db
from app.entities.task_tag import TaskTagEntity

class TaskTagRepository:
    def __init__(self):
        self.collection = db["tasks_tags"]

    async def add_relationship(self, relationship: TaskTagEntity) -> dict:
        rel_dict = relationship.dict()
        result = await self.collection.insert_one(rel_dict)
        rel_dict["_id"] = str(result.inserted_id)
        return rel_dict

    async def get_task_tags(self, task_id: str):
        tags = []
        cursor = self.collection.find({"task_id": task_id})
        async for doc in cursor:
            tags.append(doc)
        return tags
