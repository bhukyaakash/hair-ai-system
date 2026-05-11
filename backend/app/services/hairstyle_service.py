"""Hairstyle Recommendation Service"""

from typing import Optional, List
from fastapi import UploadFile
from ..ml.preprocessing.image_processing import ImagePreprocessor
from ..ml.utils.model_loader import ModelLoader


class HairstyleService:
    """Service for hairstyle recommendations"""
    
    @staticmethod
    async def recommend_hairstyles(
        file: UploadFile,
        category: Optional[str] = None,
        limit: int = 5
    ) -> dict:
        """
        Get hairstyle recommendations based on face image
        """
        # Read and process image
        contents = await file.read()
        image = ImagePreprocessor.process_image_file(contents)
        
        # Get face shape first
        face_model = ModelLoader.get_model("face_shape")
        if face_model is None:
            return {"error": "Models not loaded"}
        
        face_result = face_model.predict(image)
        face_shape = face_result["face_shape"]
        
        # Get hairstyle recommendations
        hairstyle_model = ModelLoader.get_model("hairstyle")
        if hairstyle_model is None:
            return {"error": "Hairstyle model not loaded"}
        
        recommendations = hairstyle_model.recommend(
            image,
            face_shape,
            top_n=limit
        )
        
        # Filter by category if provided
        if category:
            recommendations = [
                r for r in recommendations
                if r["category"] == category
            ]
        
        return {
            "face_shape": face_shape,
            "recommendations": recommendations[:limit],
            "total_recommendations": len(recommendations)
        }
