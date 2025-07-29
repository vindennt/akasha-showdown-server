from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    app_name: str = "Akasha Showdown Server"
    port: int = 80
    web_origin: str = "http://localhost:3000"
    database_url: str = "postgresql://user:password@localhost/dbname"

    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()