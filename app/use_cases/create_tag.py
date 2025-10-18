from app.repositories.tag_repository import TagRepository
from app.schemas.tag import TagCreateSchema, TagResponseSchema
from app.entities.tag import TagEntity

class CreateTagUseCase:
    def __init__(self, tag_repo: TagRepository):
        self.tag_repo = tag_repo

    async def execute(self, tag_data: TagCreateSchema) -> TagResponseSchema:
        tag_entity = TagEntity(name=tag_data.name)
        created_tag_dict = await self.tag_repo.create_tag(tag_entity)
        return TagResponseSchema.model_validate(created_tag_dict)
