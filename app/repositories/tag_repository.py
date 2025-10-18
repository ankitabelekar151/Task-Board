from typing import Optional
from bson import ObjectId
from app.db import db
from app.entities.tag import TagEntity

class TagRepository:
    def __init__(self):
        self.collection = db["tags"]

    async def create_tag(self, tag: TagEntity) -> dict:
        tag_dict = tag.dict(by_alias=True, exclude_unset=True)
        result = await self.collection.insert_one(tag_dict)
        tag_dict["_id"] = str(result.inserted_id)
        return tag_dict

    async def get_tag(self, tag_id: str) -> Optional[TagEntity]:
        data = await self.collection.find_one({"_id": ObjectId(tag_id)})
        if data:
            return TagEntity(**data)
        return None

    async def list_tags(self):
        tags = []
        cursor = self.collection.find()
        async for doc in cursor:
            tags.append(TagEntity(**doc))
        return tags
