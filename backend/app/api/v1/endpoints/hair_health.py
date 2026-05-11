from fastapi import APIRouter
from pydantic import BaseModel, Field

from app.models.schemas import HairHealthResponse
from app.services.hair_health_service import HairHealthService

router = APIRouter(prefix="/hair-health", tags=["hair-health"])


class HairHealthRequest(BaseModel):
    image_base64: str = Field(..., min_length=8)


@router.post("/assess", response_model=HairHealthResponse)
async def assess_hair_health(payload: HairHealthRequest):
    status, score, notes = HairHealthService.assess(payload.image_base64)
    return HairHealthResponse(status=status, score=score, notes=notes)
