"""Hairstyle Recommendation Endpoints"""

from fastapi import APIRouter, File, UploadFile, Query
from typing import List, Optional
from pydantic import BaseModel

router = APIRouter()


class HairstyleRecommendation(BaseModel):
    """Hairstyle recommendation"""
    id: str
    name: str
    description: str
    category: str  # modern, futuristic, old, present, old_age
    compatibility_score: float
    image_url: Optional[str] = None
    maintenance_level: str  # low, medium, high
    best_for: List[str]


class RecommendationResponse(BaseModel):
    """Hairstyle recommendation response"""
    face_shape: str
    recommendations: List[HairstyleRecommendation]
    total_recommendations: int


@router.post("/recommend", response_model=RecommendationResponse)
async def recommend_hairstyles(
    file: UploadFile = File(...),
    category: Optional[str] = Query(None, description="Filter by category"),
    limit: int = Query(5, ge=1, le=10)
):
    """
    Get hairstyle recommendations based on face shape
    
    - **file**: Face image for analysis
    - **category**: Filter recommendations by category (modern, futuristic, old, present, old_age)
    - **limit**: Maximum number of recommendations (1-10)
    
    Returns list of recommended hairstyles with compatibility scores
    """
    # TODO: Implement hairstyle recommendation logic
    return RecommendationResponse(
        face_shape="oval",
        recommendations=[
            HairstyleRecommendation(
                id="h1",
                name="Long Waves",
                description="Long wavy hairstyle with natural texture",
                category="modern",
                compatibility_score=0.95,
                image_url="/images/hairstyles/long-waves.jpg",
                maintenance_level="medium",
                best_for=["oval", "heart"]
            ),
            HairstyleRecommendation(
                id="h2",
                name="Bob Cut",
                description="Classic bob hairstyle",
                category="present",
                compatibility_score=0.88,
                image_url="/images/hairstyles/bob-cut.jpg",
                maintenance_level="low",
                best_for=["oval", "square"]
            )
        ],
        total_recommendations=2
    )


@router.get("/categories")
async def get_hairstyle_categories():
    """
    Get all hairstyle categories
    """
    return {
        "categories": [
            {"name": "modern", "description": "Contemporary hairstyles"},
            {"name": "futuristic", "description": "Trendy, avant-garde styles"},
            {"name": "old", "description": "Classic, vintage styles"},
            {"name": "present", "description": "Current mainstream styles"},
            {"name": "old_age", "description": "Styles suitable for mature individuals"}
        ]
    }


@router.get("/gallery")
async def get_hairstyle_gallery(
    category: Optional[str] = Query(None),
    skip: int = Query(0, ge=0),
    limit: int = Query(20, ge=1, le=100)
):
    """
    Get hairstyle gallery with filtering options
    """
    return {
        "total": 0,
        "hairstyles": []
    }
