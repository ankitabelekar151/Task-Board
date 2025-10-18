from app.repositories.task_repository import TaskRepository

class UpdateTaskStatusUseCase:
    def __init__(self, task_repo: TaskRepository):
        self.task_repo = task_repo

    async def execute(self, task_id: str, new_status: str):
        success = await self.task_repo.update_task_status(task_id, new_status)
        if not success:
            raise ValueError("Task not found or not updated")
        return {"message": "Task status updated successfully"}
