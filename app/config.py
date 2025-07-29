from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    app_name: str = "Akasha Showdown Server"
    web_origin: str = "http://localhost:3000"
    port: int = 80

    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()