"""Feature Extraction Module"""

import cv2
import numpy as np
from typing import List, Tuple


class FeatureExtractor:
    """Extract features from images"""
    
    @staticmethod
    def extract_hog_features(image: np.ndarray) -> np.ndarray:
        """
        Extract Histogram of Oriented Gradients (HOG) features
        """
        hog = cv2.HOGDescriptor(
            (224, 224),
            (16, 16),
            (8, 8),
            (8, 8),
            9
        )
        
        # Convert to grayscale if color
        if len(image.shape) == 3:
            image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        features = hog.compute(image)
        return features.flatten()
    
    @staticmethod
    def extract_color_histogram(image: np.ndarray, bins: int = 256) -> np.ndarray:
        """
        Extract color histogram features
        """
        histograms = []
        
        for i in range(image.shape[2]):
            hist = cv2.calcHist(
                [image],
                [i],
                None,
                [bins],
                [0, 256]
            )
            histograms.append(hist.flatten())
        
        return np.concatenate(histograms)
    
    @staticmethod
    def extract_edge_features(image: np.ndarray) -> np.ndarray:
        """
        Extract edge features using Canny edge detection
        """
        if len(image.shape) == 3:
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        else:
            gray = image
        
        edges = cv2.Canny(gray, 100, 200)
        return edges.flatten()
    
    @staticmethod
    def extract_lbp_features(image: np.ndarray) -> np.ndarray:
        """
        Extract Local Binary Pattern (LBP) features
        """
        from skimage import feature
        
        if len(image.shape) == 3:
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        else:
            gray = image
        
        lbp = feature.local_binary_pattern(gray, 8, 1, method='uniform')
        hist, _ = np.histogram(lbp, bins=59, range=(0, 59))
        return hist
    
    @staticmethod
    def extract_facial_landmarks(image: np.ndarray) -> List[Tuple[int, int]]:
        """
        Extract facial landmarks
        """
        # Using dlib for facial landmarks
        try:
            import dlib
            detector = dlib.get_frontal_face_detector()
            predictor = dlib.shape_predictor(
                "models/shape_predictor_68_face_landmarks.dat"
            )
            
            if len(image.shape) == 3:
                gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            else:
                gray = image
            
            dets = detector(gray, 1)
            
            landmarks = []
            for det in dets:
                shape = predictor(gray, det)
                for i in range(68):
                    x = shape.part(i).x
                    y = shape.part(i).y
                    landmarks.append((x, y))
            
            return landmarks
        except:
            return []
