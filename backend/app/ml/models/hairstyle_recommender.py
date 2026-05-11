"""Hairstyle Recommender Model"""

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import numpy as np
from typing import List, Tuple


class HairstyleRecommender:
    """Hairstyle recommendation model"""
    
    def __init__(self, model_path: str = None, input_shape: Tuple = (224, 224, 3)):
        self.input_shape = input_shape
        self.model_path = model_path
        self.categories = ["modern", "futuristic", "old", "present", "old_age"]
        self.model = None
        
        if model_path:
            self.load_model(model_path)
        else:
            self.build_model()
    
    def build_model(self):
        """
        Build hairstyle classification model
        """
        # Load pretrained MobileNetV2
        base_model = keras.applications.MobileNetV2(
            input_shape=self.input_shape,
            include_top=False,
            weights='imagenet'
        )
        
        # Freeze base model
        base_model.trainable = False
        
        # Build custom head
        inputs = keras.Input(shape=self.input_shape)
        x = keras.applications.mobilenet_v2.preprocess_input(inputs)
        x = base_model(x, training=False)
        x = layers.GlobalAveragePooling2D()(x)
        x = layers.Dense(256, activation='relu')(x)
        x = layers.BatchNormalization()(x)
        x = layers.Dropout(0.4)(x)
        x = layers.Dense(128, activation='relu')(x)
        x = layers.BatchNormalization()(x)
        x = layers.Dropout(0.3)(x)
        x = layers.Dense(64, activation='relu')(x)
        outputs = layers.Dense(len(self.categories), activation='softmax')(x)
        
        self.model = keras.Model(inputs, outputs)
        
        # Compile
        self.model.compile(
            optimizer=keras.optimizers.Adam(learning_rate=0.0005),
            loss='categorical_crossentropy',
            metrics=['accuracy', keras.metrics.AUC()]
        )
    
    def recommend(self, image: np.ndarray, face_shape: str, top_n: int = 5) -> List[dict]:
        """
        Recommend hairstyles based on image and face shape
        
        Args:
            image: Image array (224, 224, 3)
            face_shape: Detected face shape
            top_n: Number of recommendations
        
        Returns:
            List of recommendations with scores
        """
        # Preprocess
        image = np.expand_dims(image, axis=0)
        image = keras.applications.mobilenet_v2.preprocess_input(image)
        
        # Predict
        predictions = self.model.predict(image, verbose=0)[0]
        
        # Get top recommendations
        top_indices = np.argsort(predictions)[::-1][:top_n]
        recommendations = []
        
        for idx in top_indices:
            recommendations.append({
                "category": self.categories[idx],
                "compatibility_score": float(predictions[idx]),
                "face_shape": face_shape
            })
        
        return recommendations
    
    def save_model(self, path: str):
        """
        Save model to TFLite format
        """
        converter = tf.lite.TFLiteConverter.from_keras_model(self.model)
        converter.optimizations = [tf.lite.Optimize.DEFAULT]
        tflite_model = converter.convert()
        
        with open(f"{path}/hairstyle_classifier.tflite", 'wb') as f:
            f.write(tflite_model)
        
        print(f"✓ Model saved to {path}/hairstyle_classifier.tflite")
