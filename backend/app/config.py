"""Application Configuration"""

import os
from typing import List
from pydantic_settings import BaseSettings
from pydantic import Field


class Settings(BaseSettings):
    """Application settings"""
    
    # Application
    APP_NAME: str = "Hair AI Recommendation System"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = Field(default=False, env="DEBUG")
    ENVIRONMENT: str = Field(default="development", env="ENVIRONMENT")
    LOG_LEVEL: str = Field(default="INFO", env="LOG_LEVEL")
    
    # Server
    HOST: str = Field(default="0.0.0.0", env="BACKEND_HOST")
    PORT: int = Field(default=8000, env="BACKEND_PORT")
    WORKERS: int = Field(default=4, env="BACKEND_WORKERS")
    
    # Database
    DATABASE_URL: str = Field(
        default="postgresql://user:password@localhost:5432/hair_ai_db",
        env="DATABASE_URL"
    )
    DATABASE_ECHO: bool = Field(default=False, env="DATABASE_ECHO")
    
    # JWT
    SECRET_KEY: str = Field(default="your-secret-key-change-in-production", env="SECRET_KEY")
    ALGORITHM: str = Field(default="HS256", env="ALGORITHM")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = Field(default=30, env="ACCESS_TOKEN_EXPIRE_MINUTES")
    
    # CORS
    CORS_ORIGINS: List[str] = Field(
        default=["http://localhost:3000", "http://localhost:8000"],
        env="CORS_ORIGINS"
    )
    
    # ML Models
    MODEL_PATH: str = Field(default="/app/ml/saved_models", env="MODEL_PATH")
    MAX_IMAGE_SIZE: int = Field(default=10485760, env="MAX_IMAGE_SIZE")  # 10MB
    ALLOWED_IMAGE_TYPES: List[str] = Field(
        default=["jpg", "jpeg", "png"],
        env="ALLOWED_IMAGE_TYPES"
    )
    IMAGE_SIZE: tuple = (224, 224)
    
    # Cloud Storage (Google Cloud)
    GCP_PROJECT_ID: str = Field(default="", env="GCP_PROJECT_ID")
    GCP_BUCKET_NAME: str = Field(default="", env="GCP_BUCKET_NAME")
    GCP_REGION: str = Field(default="us-central1", env="GCP_REGION")
    
    # Cloud Storage (AWS)
    AWS_ACCESS_KEY_ID: str = Field(default="", env="AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY: str = Field(default="", env="AWS_SECRET_ACCESS_KEY")
    AWS_S3_BUCKET: str = Field(default="", env="AWS_S3_BUCKET")
    AWS_REGION: str = Field(default="us-east-1", env="AWS_REGION")
    
    # Email Configuration
    SMTP_SERVER: str = Field(default="smtp.gmail.com", env="SMTP_SERVER")
    SMTP_PORT: int = Field(default=587, env="SMTP_PORT")
    SMTP_USER: str = Field(default="", env="SMTP_USER")
    SMTP_PASSWORD: str = Field(default="", env="SMTP_PASSWORD")
    SMTP_FROM: str = Field(default="noreply@hairai.com", env="SMTP_FROM")
    
    # Frontend
    FRONTEND_URL: str = Field(default="http://localhost:3000", env="FRONTEND_URL")
    API_URL: str = Field(default="http://localhost:8000", env="API_URL")
    
    # Kaggle
    KAGGLE_USERNAME: str = Field(default="", env="KAGGLE_USERNAME")
    KAGGLE_KEY: str = Field(default="", env="KAGGLE_KEY")
    
    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()
