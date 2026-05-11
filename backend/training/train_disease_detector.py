"""Train Disease Detection Model"""

import tensorflow as tf
from tensorflow import keras
import numpy as np
from pathlib import Path
import json
import logging
from data_loader import DataLoader
from callbacks import get_callbacks
from metrics import MetricsCalculator
from ..app.ml.models.disease_detector import DiseaseDetector

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Configuration
BATCH_SIZE = 32
EPOCHS = 50
VALIDATION_SPLIT = 0.2
TEST_SPLIT = 0.1
IMAGE_SIZE = (224, 224)

# Data paths
DATA_DIR = "datasets/diseases"
TRAIN_LABELS = "datasets/diseases/train_labels.csv"
MODEL_SAVE_PATH = "app/ml/saved_models"


def train_disease_detector_model():
    """
    Train disease detector model
    """
    logger.info("🚀 Starting Disease Detector Training...")
    
    # Create data loader
    data_loader = DataLoader(
        data_path=DATA_DIR,
        batch_size=BATCH_SIZE,
        image_size=IMAGE_SIZE
    )
    
    # Load datasets
    logger.info("📊 Loading training data...")
    try:
        train_dataset, val_dataset, test_dataset = data_loader.create_dataset(
            images_dir=DATA_DIR,
            labels_file=TRAIN_LABELS,
            validation_split=VALIDATION_SPLIT,
            test_split=TEST_SPLIT
        )
        logger.info("✓ Data loaded successfully")
    except Exception as e:
        logger.error(f"Failed to load data: {e}")
        return
    
    # Build model
    logger.info("🏗️  Building model...")
    model = DiseaseDetector()
    logger.info(f"Model summary:")
    model.model.summary()
    
    # Get callbacks
    callbacks = get_callbacks("disease_detector")
    
    # Train model
    logger.info("⚙️  Training model...")
    history = model.model.fit(
        train_dataset,
        validation_data=val_dataset,
        epochs=EPOCHS,
        callbacks=callbacks,
        verbose=1
    )
    
    # Evaluate on test set
    logger.info("🧪 Evaluating on test set...")
    test_loss, test_accuracy, test_auc = model.model.evaluate(test_dataset)
    logger.info(f"Test Loss: {test_loss:.4f}")
    logger.info(f"Test Accuracy: {test_accuracy:.4f}")
    logger.info(f"Test AUC: {test_auc:.4f}")
    
    # Save model
    logger.info("💾 Saving model...")
    Path(MODEL_SAVE_PATH).mkdir(exist_ok=True, parents=True)
    model.save_model(MODEL_SAVE_PATH)
    
    # Save metrics
    metrics = {
        "test_loss": float(test_loss),
        "test_accuracy": float(test_accuracy),
        "test_auc": float(test_auc),
        "training_epochs": EPOCHS,
        "batch_size": BATCH_SIZE
    }
    
    with open(f"{MODEL_SAVE_PATH}/disease_detector_metrics.json", 'w') as f:
        json.dump(metrics, f, indent=2)
    
    logger.info("✅ Training completed successfully!")
    return model


if __name__ == "__main__":
    train_disease_detector_model()
