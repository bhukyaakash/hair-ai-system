"""Image Utility Functions"""

import cv2
import numpy as np
from PIL import Image
import io
from fastapi import UploadFile
from ..config import settings


async def process_image(file: UploadFile) -> np.ndarray:
    """
    Process uploaded image for ML model
    """
    contents = await file.read()
    image = Image.open(io.BytesIO(contents))
    image_array = np.array(image)
    
    # Resize to model input size
    image_resized = cv2.resize(image_array, settings.IMAGE_SIZE)
    
    # Normalize
    image_normalized = image_resized / 255.0
    
    return image_normalized


def save_uploaded_image(file_path: str, image: np.ndarray):
    """
    Save image to disk
    """
    cv2.imwrite(file_path, image)


def get_image_metadata(image_path: str) -> dict:
    """
    Extract image metadata
    """
    image = cv2.imread(image_path)
    height, width = image.shape[:2]
    
    return {
        "width": width,
        "height": height,
        "aspect_ratio": width / height
    }
