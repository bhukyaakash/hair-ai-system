from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Hair AI System"
    api_v1_prefix: str = "/api/v1"
    debug: bool = False
    database_url: str = "postgresql://postgres:postgres@localhost:5432/hair_ai"
    secret_key: str = "change-me"
    allowed_origins: list[str] = ["*"]

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


settings = Settings()
