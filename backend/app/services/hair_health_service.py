"""Hair Health Assessment Service"""

from typing import List
from fastapi import UploadFile
from ..ml.preprocessing.image_processing import ImagePreprocessor
from ..ml.utils.model_loader import ModelLoader
import numpy as np


class HairHealthService:
    """Service for hair health assessment"""
    
    @staticmethod
    async def assess_hair_health(files: List[UploadFile]) -> dict:
        """
        Assess hair health from multiple images
        """
        images = []
        
        # Process all images
        for file in files:
            contents = await file.read()
            image = ImagePreprocessor.process_image_file(contents)
            images.append(image)
        
        # Get models
        health_model = ModelLoader.get_model("hair_health")
        disease_model = ModelLoader.get_model("disease_detection")
        
        if health_model is None:
            return {"error": "Health model not loaded"}
        
        # Assess health
        health_result = health_model.assess(images)
        
        # Detect diseases
        diseases = []
        if disease_model:
            for image in images:
                disease_result = disease_model.detect(image)
                diseases.extend(disease_result["detected_diseases"])
        
        return {
            "health_score": health_result["health_score"],
            "primary_condition": health_result["primary_condition"],
            "confidence": health_result["confidence"],
            "detected_diseases": diseases,
            "recommendations": HairHealthService._get_recommendations(
                health_result["primary_condition"],
                diseases
            )
        }
    
    @staticmethod
    def _get_recommendations(condition: str, diseases: List[dict]) -> List[str]:
        """
        Get product recommendations based on condition and diseases
        """
        recommendations = []
        
        # Condition-based recommendations
        condition_map = {
            "dry": [
                "Hydrating Shampoo",
                "Deep Conditioning Treatment",
                "Hair Oil",
                "Leave-in Conditioner"
            ],
            "oily": [
                "Clarifying Shampoo",
                "Lightweight Conditioner",
                "Dry Shampoo",
                "Scalp Tonic"
            ],
            "damaged": [
                "Repair Serum",
                "Protein Treatment",
                "Hair Mask",
                "Heat Protectant"
            ]
        }
        
        recommendations.extend(condition_map.get(condition, []))
        
        # Disease-based recommendations
        disease_map = {
            "dandruff": ["Anti-Dandruff Shampoo", "Scalp Treatment"],
            "alopecia": ["Hair Growth Serum", "Scalp Stimulator"],
            "psoriasis": ["Medical Shampoo", "Scalp Lotion"],
            "eczema": ["Soothing Shampoo", "Hydrating Treatment"]
        }
        
        for disease in diseases:
            disease_name = disease.get("disease", "")
            recommendations.extend(disease_map.get(disease_name, []))
        
        # Remove duplicates
        return list(set(recommendations))[:5]
