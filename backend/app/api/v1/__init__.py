"""API v1 Package"""

from fastapi import APIRouter
from .endpoints import face_shape, hairstyle, hair_health, appointments, auth

api_router = APIRouter()

# Include routers
api_router.include_router(auth.router, prefix="/auth", tags=["Authentication"])
api_router.include_router(face_shape.router, prefix="/face-shape", tags=["Face Shape Detection"])
api_router.include_router(hairstyle.router, prefix="/hairstyle", tags=["Hairstyle Recommendation"])
api_router.include_router(hair_health.router, prefix="/hair-health", tags=["Hair Health Assessment"])
api_router.include_router(appointments.router, prefix="/appointments", tags=["Appointments"])

__all__ = ["api_router"]
