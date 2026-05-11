"""Pydantic Schemas"""

from pydantic import BaseModel, EmailStr, Field
from typing import Optional, List
from datetime import datetime


class UserCreate(BaseModel):
    """User creation schema"""
    email: EmailStr
    password: str = Field(..., min_length=8)
    full_name: str


class UserResponse(BaseModel):
    """User response schema"""
    id: str
    email: EmailStr
    full_name: str
    created_at: datetime

    class Config:
        from_attributes = True


class FaceShapeAnalysis(BaseModel):
    """Face shape analysis schema"""
    face_detected: bool
    face_shape: Optional[str] = None
    confidence: Optional[float] = None


class HairstyleRecommendation(BaseModel):
    """Hairstyle recommendation schema"""
    id: str
    name: str
    description: str
    category: str
    compatibility_score: float
    image_url: Optional[str] = None


class HairHealthAssessment(BaseModel):
    """Hair health assessment schema"""
    health_score: float
    hair_thickness: str
    hair_condition: str
    scalp_condition: str
    issues: List[dict]
    recommendations: List[str]
