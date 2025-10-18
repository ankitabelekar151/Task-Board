from fastapi import APIRouter, Depends, HTTPException
from app.use_cases.create_tag import CreateTagUseCase
from app.schemas.tag import TagCreateSchema, TagResponseSchema
from app.container import get_container

router = APIRouter()

@router.post("/tags", response_model=TagResponseSchema)
async def create_tag(
    tag_data: TagCreateSchema,
    container = Depends(get_container)
):
    use_case: CreateTagUseCase = container.resolve(CreateTagUseCase)
    try:
        created_tag = await use_case.execute(tag_data)
        return created_tag
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
