from fastapi import FastAPI
from app.controllers import task_controller, category_controller, tag_controller

app = FastAPI(title="TaskBoard API")

app.include_router(task_controller.router)
app.include_router(category_controller.router)
app.include_router(tag_controller.router)
