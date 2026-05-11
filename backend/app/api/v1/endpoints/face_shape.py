from fastapi import APIRouter

from app.models.schemas import FaceShapeRequest, FaceShapeResponse
from app.services.face_shape_service import FaceShapeService

router = APIRouter(prefix="/face-shape", tags=["face-shape"])


@router.post("/analyze", response_model=FaceShapeResponse)
async def analyze_face_shape(payload: FaceShapeRequest):
    face_shape, confidence = FaceShapeService.detect_face_shape(payload.image_base64)
    return FaceShapeResponse(face_shape=face_shape, confidence=confidence)
