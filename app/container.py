from punq import Container
from app.repositories.task_repository import TaskRepository
from app.repositories.category_repository import CategoryRepository
from app.repositories.tag_repository import TagRepository

from app.use_cases.create_task import CreateTaskUseCase
from app.use_cases.list_task import ListTasksUseCase
from app.use_cases.update_task_status import UpdateTaskStatusUseCase
from app.use_cases.create_category import CreateCategoryUseCase
from app.use_cases.create_tag import CreateTagUseCase
from app.use_cases.delete_task import DeleteTaskUseCase



container = Container()

# Repositories
container.register(TaskRepository)
container.register(CategoryRepository)
container.register(TagRepository)

# Use Cases
container.register(CreateTaskUseCase, lifetime="scoped")
container.register(ListTasksUseCase, lifetime="scoped")
container.register(UpdateTaskStatusUseCase, lifetime="scoped")
container.register(CreateCategoryUseCase, lifetime="scoped")
container.register(CreateTagUseCase, lifetime="scoped")
container.register(DeleteTaskUseCase, lifetime="scoped")



def get_container():
    return container
