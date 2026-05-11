from fastapi import APIRouter, Query

from app.models.enums import FaceShape
from app.models.schemas import HairstyleRecommendationResponse
from app.services.hairstyle_service import HairstyleService

router = APIRouter(prefix="/hairstyles", tags=["hairstyles"])


@router.get("/recommend", response_model=HairstyleRecommendationResponse)
async def recommend_hairstyles(face_shape: FaceShape = Query(...)):
    recommendations = HairstyleService.recommend(face_shape)
    return HairstyleRecommendationResponse(face_shape=face_shape, recommendations=recommendations)
