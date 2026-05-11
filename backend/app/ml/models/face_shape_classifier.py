"""Face Shape Classifier Model"""

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import numpy as np
from typing import Tuple


class FaceShapeClassifier:
    """Face shape classification model using EfficientNet"""
    
    def __init__(self, model_path: str = None, input_shape: Tuple = (224, 224, 3)):
        self.input_shape = input_shape
        self.model_path = model_path
        self.face_shapes = ["round", "oval", "square", "heart", "oblong", "diamond"]
        self.model = None
        
        if model_path:
            self.load_model(model_path)
        else:
            self.build_model()
    
    def build_model(self):
        """
        Build face shape classification model
        """
        # Load pretrained EfficientNetB0
        base_model = keras.applications.EfficientNetB0(
            input_shape=self.input_shape,
            include_top=False,
            weights='imagenet'
        )
        
        # Freeze base model layers
        base_model.trainable = False
        
        # Build custom head
        inputs = keras.Input(shape=self.input_shape)
        x = keras.applications.efficientnet.preprocess_input(inputs)
        x = base_model(x, training=False)
        x = layers.GlobalAveragePooling2D()(x)
        x = layers.Dense(256, activation='relu')(x)
        x = layers.BatchNormalization()(x)
        x = layers.Dropout(0.3)(x)
        x = layers.Dense(128, activation='relu')(x)
        x = layers.BatchNormalization()(x)
        x = layers.Dropout(0.2)(x)
        outputs = layers.Dense(len(self.face_shapes), activation='softmax')(x)
        
        self.model = keras.Model(inputs, outputs)
        
        # Compile model
        self.model.compile(
            optimizer=keras.optimizers.Adam(learning_rate=0.001),
            loss='categorical_crossentropy',
            metrics=['accuracy', keras.metrics.AUC()]
        )
    
    def predict(self, image: np.ndarray) -> dict:
        """
        Predict face shape from image
        
        Args:
            image: Image array (224, 224, 3)
        
        Returns:
            dict: Prediction with shape and confidence
        """
        # Preprocess image
        image = np.expand_dims(image, axis=0)
        image = keras.applications.efficientnet.preprocess_input(image)
        
        # Predict
        predictions = self.model.predict(image, verbose=0)
        confidence = float(np.max(predictions[0]))
        face_shape_idx = int(np.argmax(predictions[0]))
        face_shape = self.face_shapes[face_shape_idx]
        
        return {
            "face_shape": face_shape,
            "confidence": confidence,
            "all_predictions": {
                shape: float(prob) for shape, prob in zip(self.face_shapes, predictions[0])
            }
        }
    
    def save_model(self, path: str):
        """
        Save model to TFLite format
        """
        # Convert to TFLite
        converter = tf.lite.TFLiteConverter.from_keras_model(self.model)
        converter.optimizations = [tf.lite.Optimize.DEFAULT]
        tflite_model = converter.convert()
        
        # Save
        with open(f"{path}/face_shape_model.tflite", 'wb') as f:
            f.write(tflite_model)
        
        print(f"✓ Model saved to {path}/face_shape_model.tflite")
    
    def load_model(self, path: str):
        """
        Load TFLite model
        """
        interpreter = tf.lite.Interpreter(model_path=f"{path}/face_shape_model.tflite")
        interpreter.allocate_tensors()
        self.interpreter = interpreter
