"""Image Preprocessing Module"""

import cv2
import numpy as np
from PIL import Image
import io
from typing import Tuple


class ImagePreprocessor:
    """Image preprocessing utilities"""
    
    @staticmethod
    def resize_image(image: np.ndarray, target_size: Tuple = (224, 224)) -> np.ndarray:
        """
        Resize image to target size
        """
        return cv2.resize(image, target_size)
    
    @staticmethod
    def normalize_image(image: np.ndarray) -> np.ndarray:
        """
        Normalize image to [0, 1] range
        """
        return image.astype(np.float32) / 255.0
    
    @staticmethod
    def augment_image(image: np.ndarray) -> np.ndarray:
        """
        Apply data augmentation to image
        """
        # Random rotation
        angle = np.random.randint(-15, 15)
        h, w = image.shape[:2]
        M = cv2.getRotationMatrix2D((w/2, h/2), angle, 1.0)
        image = cv2.warpAffine(image, M, (w, h))
        
        # Random horizontal flip
        if np.random.random() > 0.5:
            image = cv2.flip(image, 1)
        
        # Random brightness
        brightness_factor = np.random.uniform(0.8, 1.2)
        image = np.clip(image * brightness_factor, 0, 255).astype(np.uint8)
        
        return image
    
    @staticmethod
    def detect_face(image: np.ndarray) -> Tuple[bool, np.ndarray]:
        """
        Detect face in image using Haar Cascade
        """
        face_cascade = cv2.CascadeClassifier(
            cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
        )
        
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30)
        )
        
        if len(faces) > 0:
            x, y, w, h = faces[0]
            face_image = image[y:y+h, x:x+w]
            return True, face_image
        
        return False, image
    
    @staticmethod
    def process_image_file(file_contents: bytes, target_size: Tuple = (224, 224)) -> np.ndarray:
        """
        Process uploaded image file
        """
        image = Image.open(io.BytesIO(file_contents))
        image_array = np.array(image)
        
        # Convert to BGR if RGB
        if len(image_array.shape) == 3 and image_array.shape[2] == 3:
            image_array = cv2.cvtColor(image_array, cv2.COLOR_RGB2BGR)
        
        # Detect and crop face
        face_detected, face_image = ImagePreprocessor.detect_face(image_array)
        
        # Resize
        resized = ImagePreprocessor.resize_image(face_image, target_size)
        
        # Normalize
        normalized = ImagePreprocessor.normalize_image(resized)
        
        return normalized
