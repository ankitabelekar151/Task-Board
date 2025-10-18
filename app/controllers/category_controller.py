from fastapi import APIRouter, Depends, HTTPException
from app.use_cases.create_category import CreateCategoryUseCase
from app.schemas.category import CategoryCreateSchema, CategoryResponseSchema
from app.container import get_container

router = APIRouter()

@router.post("/categories", response_model=CategoryResponseSchema)
async def create_category(
    category_data: CategoryCreateSchema,
    container = Depends(get_container)
):
    use_case: CreateCategoryUseCase = container.resolve(CreateCategoryUseCase)
    try:
        created_category = await use_case.execute(category_data)
        return created_category
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
