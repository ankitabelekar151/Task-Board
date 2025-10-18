from typing import List, Optional
from bson import ObjectId
from app.db import db
from app.entities.task import TaskEntity
import base64
import binascii


class TaskRepository:
    def __init__(self):
        self.collection = db["tasks"]

    async def create_task(self, task: TaskEntity) -> dict:
        task_dict = task.model_dump(by_alias=True, exclude_unset=True)

        task_dict.setdefault("status", task.status or "pending")
        task_dict.setdefault("deleted", task.deleted or False)

        # Convert category_ids and tag_ids to ObjectId for storage
        category_ids = [ObjectId(cid) for cid in task.category_ids] if task.category_ids else []
        tag_ids = [ObjectId(tid) for tid in task.tag_ids] if task.tag_ids else []

        result = await self.collection.insert_one(task_dict)
        task_id = result.inserted_id
        task_dict["_id"] = str(task_id)

        # Insert into relationship collections
        if category_ids:
            await db["tasks_categories"].insert_many([
                {"task_id": task_id, "category_id": cid} for cid in category_ids
            ])

        if tag_ids:
            await db["tasks_tags"].insert_many([
                {"task_id": task_id, "tag_id": tid} for tid in tag_ids
            ])

        # Convert ObjectIds back to strings for JSON response
        task_dict["category_ids"] = [str(cid) for cid in category_ids]
        task_dict["tag_ids"] = [str(tid) for tid in tag_ids]

        return task_dict

    async def get_task(self, task_id: str) -> Optional[TaskEntity]:
        data = await self.collection.find_one({"_id": ObjectId(task_id), "deleted": False})
        if data:
            categories = await db["tasks_categories"].find({"task_id": task_id}).to_list(length=None)
            data["category_ids"] = [rel["category_id"] for rel in categories]

            tags = await db["tasks_tags"].find({"task_id": task_id}).to_list(length=None)
            data["tag_ids"] = [rel["tag_id"] for rel in tags]

            return TaskEntity(**data)
        return None
    async def update_task_status(self, task_id: str, status: str) -> bool:
        result = await self.collection.update_one(
            {"_id": ObjectId(task_id)},
            {"$set": {"status": status}}
        )
        return result.modified_count > 0

    async def soft_delete_task(self, task_id: str) -> bool:
        result = await self.collection.update_one(
            {"_id": ObjectId(task_id)},
            {"$set": {"deleted": True}}
        )
        return result.modified_count > 0

    async def list_tasks(
        self,
        category_id: Optional[str] = None,
        tag_id: Optional[str] = None,
        cursor: Optional[str] = None,
        limit: int = 10,
        direction: str = "forward"
    ) -> dict:
        query = {"deleted": False}

        # Cursor filter
        if cursor:
            try:
                decoded_id = base64.b64decode(cursor.encode()).decode()
                obj_id = ObjectId(decoded_id)
                cursor_filter = {"$gt": obj_id} if direction == "forward" else {"$lt": obj_id}
                if "_id" in query:
                    query["_id"].update(cursor_filter)
                else:
                    query["_id"] = cursor_filter
            except (base64.binascii.Error, ValueError):
                raise ValueError("Invalid cursor value")

        # Filter by category
        task_ids_filter = None
        if category_id:
            categories = await db["tasks_categories"].find({"category_id": ObjectId(category_id)}).to_list(length=None)
            task_ids_filter = [rel["task_id"] for rel in categories]

        # Filter by tag
        if tag_id:
            tags = await db["tasks_tags"].find({"tag_id": ObjectId(tag_id)}).to_list(length=None)
            tag_task_ids = [rel["task_id"] for rel in tags]
            if task_ids_filter is not None:
                task_ids_filter = list(set(task_ids_filter) & set(tag_task_ids))
            else:
                task_ids_filter = tag_task_ids

        # Merge cursor and $in filter
        if task_ids_filter is not None:
            object_ids = [ObjectId(tid) for tid in task_ids_filter]
            if "_id" in query:
                query["_id"] = {"$in": object_ids, **query["_id"]}
            else:
                query["_id"] = {"$in": object_ids}

        # Sorting
        sort_order = 1 if direction == "forward" else -1
        cursor_obj = self.collection.find(query).sort("_id", sort_order).limit(limit)
        tasks = []
        async for doc in cursor_obj:
            doc["_id"] = str(doc["_id"])
            doc["category_ids"] = [str(cid) for cid in doc.get("category_ids", [])]
            doc["tag_ids"] = [str(tid) for tid in doc.get("tag_ids", [])]
            tasks.append(doc)

        # Encode cursors
        next_cursor = None
        prev_cursor = None
        if tasks:
            next_cursor = base64.b64encode(tasks[-1]["_id"].encode()).decode()
            prev_cursor = base64.b64encode(tasks[0]["_id"].encode()).decode()

        return {"items": tasks, "next_cursor": next_cursor, "prev_cursor": prev_cursor}
