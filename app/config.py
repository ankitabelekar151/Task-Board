from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    MONGO_URI: str = "mongodb://localhost:27017"
    MONGO_DB: str = "taskboard"
    APP_NAME: str = "TaskBoard"

    class Config:
        env_file = ".env"

settings = Settings()
