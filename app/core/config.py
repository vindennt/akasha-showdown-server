from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import (
    AnyUrl,
    BeforeValidator,
)
from typing import Annotated, Any, Literal, Self

# Parse CORS lists from JSON form or comma-separated form
def parse_cors(v: Any) -> list[str] | str:
    if isinstance(v, str) and not v.startswith("["):
        return [i.strip() for i in v.split(",")]
    elif isinstance(v, list | str):
        return v
    raise ValueError(f"Invalid CORS value: {v}")

class Settings(BaseSettings):
    PROJECT_NAME: str = "akasha-showdown-server"
    PORT: int = 80

    FRONTEND_HOST: str = "http://localhost:3000"
    # Uses parse_cors beforehand to ensure typematch, else defaults to empty
    BACKEND_CORS_ORIGINS: Annotated[list[AnyUrl] | str, BeforeValidator(parse_cors)] = []

    SUPABASE_URL: str = "your_supabase_url"
    SUPABASE_KEY: str = "your_supabase_key"

    POSTGRES_SERVER: str = "localhost"
    POSTGRES_PORT: int = 5432
    POSTGRES_USER: str = "postgres"
    POSTGRES_PASSWORD: str = "your_password"
    POSTGRES_DB: str = "akasha_showdown"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_ignore_empty=True,
        extra="ignore",
        )

    # combine CORS origins
    @property
    def all_cors_origins(self) -> list[str]:
        return (
            [str(origin).rstrip("/") for origin in self.BACKEND_CORS_ORIGINS]
            + [self.FRONTEND_HOST.rstrip("/")]
        )

settings = Settings()