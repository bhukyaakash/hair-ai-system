"""Hair Health Assessment Endpoints"""

from fastapi import APIRouter, File, UploadFile, Query
from typing import List, Optional
from pydantic import BaseModel

router = APIRouter()


class HairIssue(BaseModel):
    """Hair/scalp issue"""
    issue_type: str  # alopecia, dandruff, psoriasis, seborrheic_dermatitis, etc.
    severity: str  # mild, moderate, severe
    description: str
    recommended_treatments: List[str]


class HairHealthReport(BaseModel):
    """Hair health assessment report"""
    hair_health_score: float  # 0-100
    hair_thickness: str  # thin, normal, thick
    hair_condition: str  # dry, normal, oily
    scalp_condition: str  # healthy, irritated, inflamed
    issues_detected: List[HairIssue]
    product_recommendations: List[str]
    professional_advice: str


@router.post("/assess", response_model=HairHealthReport)
async def assess_hair_health(files: List[UploadFile] = File(...)):
    """
    Assess hair health from multiple images
    
    - **files**: Multiple images for comprehensive analysis
    
    Returns detailed hair health report with issues and recommendations
    """
    # TODO: Implement hair health analysis using ML models
    return HairHealthReport(
        hair_health_score=75.0,
        hair_thickness="normal",
        hair_condition="slightly_dry",
        scalp_condition="healthy",
        issues_detected=[
            HairIssue(
                issue_type="mild_dryness",
                severity="mild",
                description="Hair shows signs of mild dryness",
                recommended_treatments=["deep-conditioning", "moisturizing-mask"]
            )
        ],
        product_recommendations=[
            "Hydrating Shampoo",
            "Deep Conditioning Treatment",
            "Hair Oil"
        ],
        professional_advice="Increase deep conditioning treatments twice a week"
    )


@router.get("/conditions")
async def get_hair_conditions():
    """
    Get all possible hair and scalp conditions
    """
    return {
        "conditions": [
            {"name": "alopecia", "description": "Hair loss condition"},
            {"name": "dandruff", "description": "Flaky scalp condition"},
            {"name": "psoriasis", "description": "Scalp inflammation"},
            {"name": "seborrheic_dermatitis", "description": "Oily scalp condition"},
            {"name": "eczema", "description": "Itchy scalp condition"}
        ]
    }


@router.post("/disease-detect")
async def detect_diseases(files: List[UploadFile] = File(...)):
    """
    Detect hair and scalp diseases from images
    """
    # TODO: Implement disease detection model
    return {
        "diseases_detected": [],
        "confidence": 0.0,
        "recommendation": "Consult a dermatologist for professional diagnosis"
    }


@router.get("/products")
async def get_product_recommendations(
    issue: Optional[str] = Query(None),
    price_range: Optional[str] = Query(None)  # low, medium, high
):
    """
    Get product recommendations based on hair issues
    """
    return {
        "products": [],
        "total": 0
    }
