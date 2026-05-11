from pydantic import BaseModel, Field

from app.models.enums import FaceShape, HairHealthStatus


class HealthResponse(BaseModel):
    status: str = "ok"


class FaceShapeRequest(BaseModel):
    image_base64: str = Field(..., min_length=8)


class FaceShapeResponse(BaseModel):
    face_shape: FaceShape
    confidence: float


class HairstyleRecommendationResponse(BaseModel):
    face_shape: FaceShape
    recommendations: list[str]


class HairHealthResponse(BaseModel):
    status: HairHealthStatus
    score: float
    notes: list[str] = []
