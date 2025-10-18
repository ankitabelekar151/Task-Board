from app.repositories.task_repository import TaskRepository
from app.schemas.task import TaskCreateSchema, TaskResponseSchema
from app.entities.task import TaskEntity

class CreateTaskUseCase:
    def __init__(self, task_repo: TaskRepository):
        self.task_repo = task_repo

    async def execute(self, task_data: TaskCreateSchema) -> TaskResponseSchema:
        task_entity = TaskEntity(
            title=task_data.title,
            description=task_data.description,
            due_date=task_data.due_date,
            category_ids=task_data.category_ids or [],
            tag_ids=task_data.tag_ids or []
        )
        created_task_dict = await self.task_repo.create_task(task_entity)
        return TaskResponseSchema.model_validate(created_task_dict)
