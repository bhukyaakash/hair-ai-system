"""Training Metrics Calculation"""

import numpy as np
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
    confusion_matrix,
    classification_report
)
import json


class MetricsCalculator:
    """Calculate training metrics"""
    
    @staticmethod
    def calculate_metrics(y_true, y_pred, y_pred_proba=None):
        """
        Calculate comprehensive metrics
        """
        # Convert to binary if multi-class
        if len(y_pred.shape) > 1:
            y_pred = np.argmax(y_pred, axis=1)
        if len(y_true.shape) > 1:
            y_true = np.argmax(y_true, axis=1)
        
        metrics = {
            "accuracy": float(accuracy_score(y_true, y_pred)),
            "precision": float(precision_score(y_true, y_pred, average='weighted', zero_division=0)),
            "recall": float(recall_score(y_true, y_pred, average='weighted', zero_division=0)),
            "f1_score": float(f1_score(y_true, y_pred, average='weighted', zero_division=0))
        }
        
        # ROC-AUC if probabilities available
        if y_pred_proba is not None:
            try:
                metrics["roc_auc"] = float(roc_auc_score(
                    y_true, y_pred_proba, multi_class='ovr', zero_division=0
                ))
            except:
                metrics["roc_auc"] = 0.0
        
        return metrics
    
    @staticmethod
    def get_confusion_matrix(y_true, y_pred):
        """
        Get confusion matrix
        """
        if len(y_pred.shape) > 1:
            y_pred = np.argmax(y_pred, axis=1)
        if len(y_true.shape) > 1:
            y_true = np.argmax(y_true, axis=1)
        
        return confusion_matrix(y_true, y_pred)
    
    @staticmethod
    def get_classification_report(y_true, y_pred):
        """
        Get detailed classification report
        """
        if len(y_pred.shape) > 1:
            y_pred = np.argmax(y_pred, axis=1)
        if len(y_true.shape) > 1:
            y_true = np.argmax(y_true, axis=1)
        
        return classification_report(y_true, y_pred, output_dict=True)
    
    @staticmethod
    def save_metrics(metrics: dict, filepath: str):
        """
        Save metrics to JSON file
        """
        with open(filepath, 'w') as f:
            json.dump(metrics, f, indent=2)
