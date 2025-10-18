from app.repositories.task_repository import TaskRepository
from app.schemas.task import TaskResponseSchema
from typing import Optional

class ListTasksUseCase:
    def __init__(self, task_repo: TaskRepository):
        self.task_repo = task_repo

    async def execute(
        self,
        category_id: Optional[str] = None,
        tag_id: Optional[str] = None,
        cursor: Optional[str] = None,
        limit: int = 10,
        direction: str = "forward"  # "forward" or "backward"
    ):
        result = await self.task_repo.list_tasks(
            category_id=category_id,
            tag_id=tag_id,
            cursor=cursor,
            limit=limit,
            direction=direction
        )

        items = [TaskResponseSchema.model_validate(task) for task in result["items"]]

        return {
            "items": items,
            "next_cursor": result.get("next_cursor"),
            "prev_cursor": result.get("prev_cursor")
        }
