from pathlib import Path
import unittest


class TestModelFiles(unittest.TestCase):
    def test_ml_model_files_exist(self):
        files = [
            'backend/app/ml/models/face_shape_classifier.py',
            'backend/app/ml/models/hairstyle_recommender.py',
            'backend/app/ml/models/hair_health_analyzer.py',
            'backend/app/ml/models/disease_detector.py',
        ]
        for file in files:
            with self.subTest(file=file):
                self.assertTrue(Path(file).exists())
