from app.repositories.category_repository import CategoryRepository
from app.schemas.category import CategoryCreateSchema, CategoryResponseSchema
from app.entities.category import CategoryEntity

class CreateCategoryUseCase:
    def __init__(self, category_repo: CategoryRepository):
        self.category_repo = category_repo

    async def execute(self, category_data: CategoryCreateSchema) -> CategoryResponseSchema:
        category_entity = CategoryEntity(
            name=category_data.name,
            description=category_data.description
        )
        created_category_dict = await self.category_repo.create_category(category_entity)
        return CategoryResponseSchema.model_validate(created_category_dict)
