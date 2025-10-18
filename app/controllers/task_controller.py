from fastapi import APIRouter, Depends, HTTPException, Query
from app.use_cases.create_task import CreateTaskUseCase
from app.schemas.task import TaskCreateSchema, TaskResponseSchema,TaskUpdateStatusSchema
from app.container import get_container
from typing import Optional
from app.use_cases.list_task import ListTasksUseCase
from app.use_cases.update_task_status import UpdateTaskStatusUseCase
from app.use_cases.delete_task import DeleteTaskUseCase


router = APIRouter()

@router.post("/tasks", response_model=TaskResponseSchema)
async def create_task(
    task_data: TaskCreateSchema,
    container = Depends(get_container)
):
    use_case: CreateTaskUseCase = container.resolve(CreateTaskUseCase)
    try:
        created_task = await use_case.execute(task_data)
        return created_task
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/tasks")
async def list_tasks(
    category_id: Optional[str] = Query(None),
    tag_id: Optional[str] = Query(None),
    cursor: Optional[str] = Query(None),
    limit: int = Query(10),
    container = Depends(get_container)
):
    use_case: ListTasksUseCase = container.resolve(ListTasksUseCase)
    return await use_case.execute(category_id, tag_id, cursor, limit)

@router.patch("/tasks/{task_id}/status")
async def update_task_status(
    task_id: str,
    body: TaskUpdateStatusSchema,
    container = Depends(get_container)
):
    use_case: UpdateTaskStatusUseCase = container.resolve(UpdateTaskStatusUseCase)
    try:
        result = await use_case.execute(task_id, body.status)
        return result
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.delete("/tasks/{task_id}")
async def delete_task(
    task_id: str,
    container = Depends(get_container)
):
    try:
        use_case: DeleteTaskUseCase = container.resolve(DeleteTaskUseCase)
        result = await use_case.execute(task_id)
        return result
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
