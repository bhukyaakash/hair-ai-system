"""Model Loader Utilities"""

import tensorflow as tf
from ..models.face_shape_classifier import FaceShapeClassifier
from ..models.hairstyle_recommender import HairstyleRecommender
from ..models.hair_health_analyzer import HairHealthAnalyzer
from ..models.disease_detector import DiseaseDetector
import logging

logger = logging.getLogger(__name__)


class ModelLoader:
    """Load and manage ML models"""
    
    _models = {
        "face_shape": None,
        "hairstyle": None,
        "hair_health": None,
        "disease_detection": None
    }
    
    @classmethod
    def load_all_models(cls, model_path: str):
        """
        Load all models from path
        """
        logger.info(f"Loading models from {model_path}...")
        
        try:
            cls._models["face_shape"] = FaceShapeClassifier(model_path=model_path)
            logger.info("✓ Face shape classifier loaded")
        except Exception as e:
            logger.error(f"Failed to load face shape classifier: {e}")
        
        try:
            cls._models["hairstyle"] = HairstyleRecommender(model_path=model_path)
            logger.info("✓ Hairstyle recommender loaded")
        except Exception as e:
            logger.error(f"Failed to load hairstyle recommender: {e}")
        
        try:
            cls._models["hair_health"] = HairHealthAnalyzer(model_path=model_path)
            logger.info("✓ Hair health analyzer loaded")
        except Exception as e:
            logger.error(f"Failed to load hair health analyzer: {e}")
        
        try:
            cls._models["disease_detection"] = DiseaseDetector(model_path=model_path)
            logger.info("✓ Disease detector loaded")
        except Exception as e:
            logger.error(f"Failed to load disease detector: {e}")
    
    @classmethod
    def get_model(cls, model_name: str):
        """
        Get loaded model by name
        """
        return cls._models.get(model_name)
    
    @classmethod
    def is_model_loaded(cls, model_name: str) -> bool:
        """
        Check if model is loaded
        """
        return cls._models.get(model_name) is not None
