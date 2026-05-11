"""Hair Health Analyzer Model"""

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import numpy as np
from typing import Tuple, List


class HairHealthAnalyzer:
    """Hair health assessment model"""
    
    def __init__(self, model_path: str = None, input_shape: Tuple = (224, 224, 3)):
        self.input_shape = input_shape
        self.model_path = model_path
        self.health_metrics = ["dry", "normal", "oily", "damaged", "healthy"]
        self.model = None
        
        if model_path:
            self.load_model(model_path)
        else:
            self.build_model()
    
    def build_model(self):
        """
        Build hair health classification model
        """
        # Load pretrained InceptionV3
        base_model = keras.applications.InceptionV3(
            input_shape=self.input_shape,
            include_top=False,
            weights='imagenet'
        )
        
        # Freeze base model
        base_model.trainable = False
        
        # Build custom head
        inputs = keras.Input(shape=self.input_shape)
        x = keras.applications.inception_v3.preprocess_input(inputs)
        x = base_model(x, training=False)
        x = layers.GlobalAveragePooling2D()(x)
        x = layers.Dense(512, activation='relu')(x)
        x = layers.BatchNormalization()(x)
        x = layers.Dropout(0.4)(x)
        x = layers.Dense(256, activation='relu')(x)
        x = layers.BatchNormalization()(x)
        x = layers.Dropout(0.3)(x)
        x = layers.Dense(128, activation='relu')(x)
        outputs = layers.Dense(len(self.health_metrics), activation='softmax')(x)
        
        self.model = keras.Model(inputs, outputs)
        
        # Compile
        self.model.compile(
            optimizer=keras.optimizers.Adam(learning_rate=0.0005),
            loss='categorical_crossentropy',
            metrics=['accuracy', keras.metrics.AUC()]
        )
    
    def assess(self, images: List[np.ndarray]) -> dict:
        """
        Assess hair health from multiple images
        
        Args:
            images: List of image arrays
        
        Returns:
            Health assessment report
        """
        all_predictions = []
        
        for image in images:
            # Preprocess
            image = np.expand_dims(image, axis=0)
            image = keras.applications.inception_v3.preprocess_input(image)
            
            # Predict
            predictions = self.model.predict(image, verbose=0)[0]
            all_predictions.append(predictions)
        
        # Average predictions
        avg_predictions = np.mean(all_predictions, axis=0)
        
        # Calculate health score (0-100)
        health_score = float(np.max(avg_predictions) * 100)
        primary_condition = self.health_metrics[np.argmax(avg_predictions)]
        
        return {
            "health_score": health_score,
            "primary_condition": primary_condition,
            "all_scores": {
                metric: float(score) for metric, score in zip(self.health_metrics, avg_predictions)
            },
            "confidence": float(np.max(avg_predictions))
        }
    
    def save_model(self, path: str):
        """
        Save model to TFLite format
        """
        converter = tf.lite.TFLiteConverter.from_keras_model(self.model)
        converter.optimizations = [tf.lite.Optimize.DEFAULT]
        tflite_model = converter.convert()
        
        with open(f"{path}/hair_health_model.tflite", 'wb') as f:
            f.write(tflite_model)
        
        print(f"✓ Model saved to {path}/hair_health_model.tflite")
