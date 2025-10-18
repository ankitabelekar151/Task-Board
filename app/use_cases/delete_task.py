from app.repositories.task_repository import TaskRepository

class DeleteTaskUseCase:
    def __init__(self, task_repo: TaskRepository):
        self.task_repo = task_repo

    async def execute(self, task_id: str):
        success = await self.task_repo.soft_delete_task(task_id)
        if not success:
            raise ValueError("Task not found or already deleted")
        return {"message": "Task deleted successfully"}
