# Training data loader utilities

import tensorflow as tf
import numpy as np
from pathlib import Path
from typing import Tuple, Generator
import cv2
from sklearn.model_selection import train_test_split


class DataLoader:
    """Load and prepare training data"""
    
    def __init__(self, data_path: str, batch_size: int = 32, image_size: Tuple = (224, 224)):
        self.data_path = Path(data_path)
        self.batch_size = batch_size
        self.image_size = image_size
    
    def load_image(self, image_path: str) -> np.ndarray:
        """
        Load and preprocess image
        """
        image = cv2.imread(image_path)
        image = cv2.resize(image, self.image_size)
        image = image.astype(np.float32) / 255.0
        return image
    
    def create_dataset(
        self,
        images_dir: str,
        labels_file: str,
        validation_split: float = 0.2,
        test_split: float = 0.1
    ) -> Tuple[tf.data.Dataset, tf.data.Dataset, tf.data.Dataset]:
        """
        Create train, validation, and test datasets
        """
        # Load image paths and labels
        image_paths = []
        labels = []
        
        with open(labels_file, 'r') as f:
            for line in f:
                parts = line.strip().split(',')
                image_paths.append(parts[0])
                labels.append(int(parts[1]))
        
        # Convert to numpy arrays
        image_paths = np.array(image_paths)
        labels = np.array(labels)
        
        # Split data
        train_paths, test_paths, train_labels, test_labels = train_test_split(
            image_paths, labels, test_size=test_split, random_state=42
        )
        
        train_paths, val_paths, train_labels, val_labels = train_test_split(
            train_paths, train_labels, test_size=validation_split, random_state=42
        )
        
        # Create TensorFlow datasets
        train_dataset = tf.data.Dataset.from_tensor_slices((train_paths, train_labels))
        val_dataset = tf.data.Dataset.from_tensor_slices((val_paths, val_labels))
        test_dataset = tf.data.Dataset.from_tensor_slices((test_paths, test_labels))
        
        # Preprocess and batch
        train_dataset = train_dataset.map(
            lambda x, y: (tf.py_function(self.load_image, [x], tf.float32), y),
            num_parallel_calls=tf.data.AUTOTUNE
        ).batch(self.batch_size).prefetch(tf.data.AUTOTUNE)
        
        val_dataset = val_dataset.map(
            lambda x, y: (tf.py_function(self.load_image, [x], tf.float32), y),
            num_parallel_calls=tf.data.AUTOTUNE
        ).batch(self.batch_size).prefetch(tf.data.AUTOTUNE)
        
        test_dataset = test_dataset.map(
            lambda x, y: (tf.py_function(self.load_image, [x], tf.float32), y),
            num_parallel_calls=tf.data.AUTOTUNE
        ).batch(self.batch_size).prefetch(tf.data.AUTOTUNE)
        
        return train_dataset, val_dataset, test_dataset
