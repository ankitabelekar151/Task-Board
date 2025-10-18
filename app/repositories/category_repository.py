from typing import Optional
from bson import ObjectId
from app.db import db
from app.entities.category import CategoryEntity

class CategoryRepository:
    def __init__(self):
        self.collection = db["categories"]

    async def create_category(self, category: CategoryEntity) -> dict:
        category_dict = category.dict(by_alias=True, exclude_unset=True)
        result = await self.collection.insert_one(category_dict)
        category_dict["_id"] = str(result.inserted_id)
        return category_dict

    async def get_category(self, category_id: str) -> Optional[CategoryEntity]:
        data = await self.collection.find_one({"_id": ObjectId(category_id)})
        if data:
            return CategoryEntity(**data)
        return None

    async def list_categories(self):
        categories = []
        cursor = self.collection.find()
        async for doc in cursor:
            categories.append(CategoryEntity(**doc))
        return categories
