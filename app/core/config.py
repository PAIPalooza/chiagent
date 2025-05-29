from typing import Any, Dict, Optional
from pydantic import BaseModel
from pydantic import AnyHttpUrl
from dotenv import load_dotenv
import os

load_dotenv()

class Settings(BaseModel):
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "chiagent"

    # Database
    POSTGRES_SERVER: str = os.getenv("POSTGRES_SERVER", "localhost")
    POSTGRES_USER: str = os.getenv("POSTGRES_USER", "postgres")
    POSTGRES_PASSWORD: str = os.getenv("POSTGRES_PASSWORD", "postgres")
    POSTGRES_DB: str = os.getenv("POSTGRES_DB", "chiagent")
    SQLALCHEMY_DATABASE_URI: Optional[str] = None

    @property
    def database_url(self) -> str:
        return f"postgresql://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_SERVER}/{self.POSTGRES_DB}"

    class Config:
        case_sensitive = True


settings = Settings()
