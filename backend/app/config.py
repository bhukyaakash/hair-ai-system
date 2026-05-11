from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import model_validator


class Settings(BaseSettings):
    app_name: str = "Hair AI System"
    api_v1_prefix: str = "/api/v1"
    debug: bool = False
    environment: str = "development"
    database_url: str = "postgresql://postgres:postgres@localhost:5432/hair_ai"
    secret_key: str = "change-me"
    api_key: str = "change-me-api-key"
    allowed_origins: list[str] = ["*"]

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    @model_validator(mode="after")
    def validate_secrets(self):
        is_production = self.environment.lower() == "production"
        if is_production and self.secret_key == "change-me":
            raise ValueError("SECRET_KEY must be changed for non-debug environments")
        if is_production and self.api_key == "change-me-api-key":
            raise ValueError("API_KEY must be changed for non-debug environments")
        return self


settings = Settings()
