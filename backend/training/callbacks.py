"""Training Callbacks"""

import tensorflow as tf
from tensorflow import keras
import json
from pathlib import Path


class MetricsLogger(keras.callbacks.Callback):
    """Log training metrics to JSON file"""
    
    def __init__(self, log_file: str = "training_metrics.json"):
        super().__init__()
        self.log_file = log_file
        self.metrics_history = {}
    
    def on_epoch_end(self, epoch, logs=None):
        logs = logs or {}
        
        for key, value in logs.items():
            if key not in self.metrics_history:
                self.metrics_history[key] = []
            self.metrics_history[key].append(float(value))
        
        # Save to file
        with open(self.log_file, 'w') as f:
            json.dump(self.metrics_history, f, indent=2)


def get_callbacks(model_name: str, checkpoint_dir: str = "checkpoints") -> list:
    """
    Get training callbacks
    """
    Path(checkpoint_dir).mkdir(exist_ok=True)
    
    callbacks = [
        # Early stopping
        keras.callbacks.EarlyStopping(
            monitor='val_loss',
            patience=10,
            restore_best_weights=True,
            verbose=1
        ),
        
        # Model checkpoint
        keras.callbacks.ModelCheckpoint(
            filepath=f"{checkpoint_dir}/{model_name}_best.h5",
            monitor='val_accuracy',
            save_best_only=True,
            verbose=1
        ),
        
        # Learning rate reduction
        keras.callbacks.ReduceLROnPlateau(
            monitor='val_loss',
            factor=0.5,
            patience=5,
            min_lr=1e-7,
            verbose=1
        ),
        
        # Metrics logger
        MetricsLogger(log_file=f"{checkpoint_dir}/{model_name}_metrics.json"),
        
        # TensorBoard
        keras.callbacks.TensorBoard(
            log_dir=f"logs/{model_name}",
            histogram_freq=1,
            write_graph=True
        )
    ]
    
    return callbacks
