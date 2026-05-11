"""Disease Detection Model"""

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import numpy as np
from typing import Tuple, List


class DiseaseDetector:
    """Hair and scalp disease detection model"""
    
    def __init__(self, model_path: str = None, input_shape: Tuple = (224, 224, 3)):
        self.input_shape = input_shape
        self.model_path = model_path
        self.diseases = [
            "healthy",
            "alopecia",
            "dandruff",
            "psoriasis",
            "seborrheic_dermatitis",
            "eczema",
            "ringworm"
        ]
        self.model = None
        
        if model_path:
            self.load_model(model_path)
        else:
            self.build_model()
    
    def build_model(self):
        """
        Build disease detection model
        """
        # Load pretrained ResNet50
        base_model = keras.applications.ResNet50(
            input_shape=self.input_shape,
            include_top=False,
            weights='imagenet'
        )
        
        # Freeze base model
        base_model.trainable = False
        
        # Build custom head
        inputs = keras.Input(shape=self.input_shape)
        x = keras.applications.resnet50.preprocess_input(inputs)
        x = base_model(x, training=False)
        x = layers.GlobalAveragePooling2D()(x)
        x = layers.Dense(512, activation='relu')(x)
        x = layers.BatchNormalization()(x)
        x = layers.Dropout(0.5)(x)
        x = layers.Dense(256, activation='relu')(x)
        x = layers.BatchNormalization()(x)
        x = layers.Dropout(0.4)(x)
        x = layers.Dense(128, activation='relu')(x)
        outputs = layers.Dense(len(self.diseases), activation='softmax')(x)
        
        self.model = keras.Model(inputs, outputs)
        
        # Compile
        self.model.compile(
            optimizer=keras.optimizers.Adam(learning_rate=0.0003),
            loss='categorical_crossentropy',
            metrics=['accuracy', keras.metrics.AUC()]
        )
    
    def detect(self, image: np.ndarray, threshold: float = 0.6) -> dict:
        """
        Detect diseases from image
        
        Args:
            image: Image array (224, 224, 3)
            threshold: Confidence threshold
        
        Returns:
            Disease detection report
        """
        # Preprocess
        image = np.expand_dims(image, axis=0)
        image = keras.applications.resnet50.preprocess_input(image)
        
        # Predict
        predictions = self.model.predict(image, verbose=0)[0]
        
        # Get primary disease
        primary_disease_idx = np.argmax(predictions)
        primary_disease = self.diseases[primary_disease_idx]
        confidence = float(predictions[primary_disease_idx])
        
        # Check if healthy
        if primary_disease == "healthy":
            detected_diseases = []
        else:
            detected_diseases = [
                {
                    "disease": self.diseases[idx],
                    "confidence": float(predictions[idx])
                }
                for idx in np.where(predictions > threshold)[0]
                if self.diseases[idx] != "healthy"
            ]
        
        return {
            "primary_condition": primary_disease,
            "confidence": confidence,
            "detected_diseases": detected_diseases,
            "all_scores": {
                disease: float(score) for disease, score in zip(self.diseases, predictions)
            }
        }
    
    def save_model(self, path: str):
        """
        Save model to TFLite format
        """
        converter = tf.lite.TFLiteConverter.from_keras_model(self.model)
        converter.optimizations = [tf.lite.Optimize.DEFAULT]
        converter.target_spec.supported_ops = [
            tf.lite.OpsSet.TFLITE_BUILTINS,
            tf.lite.OpsSet.SELECT_TF_OPS
        ]
        tflite_model = converter.convert()
        
        with open(f"{path}/disease_detector.tflite", 'wb') as f:
            f.write(tflite_model)
        
        print(f"✓ Model saved to {path}/disease_detector.tflite")
