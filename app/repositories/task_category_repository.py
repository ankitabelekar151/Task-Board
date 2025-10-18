from app.db import db
from app.entities.task_category import TaskCategoryEntity

class TaskCategoryRepository:
    def __init__(self):
        self.collection = db["tasks_categories"]

    async def add_relationship(self, relationship: TaskCategoryEntity) -> dict:
        rel_dict = relationship.dict()
        result = await self.collection.insert_one(rel_dict)
        rel_dict["_id"] = str(result.inserted_id)
        return rel_dict

    async def get_task_categories(self, task_id: str):
        categories = []
        cursor = self.collection.find({"task_id": task_id})
        async for doc in cursor:
            categories.append(doc)
        return categories
