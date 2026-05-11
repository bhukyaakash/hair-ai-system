from pathlib import Path
import unittest


class TestServiceFiles(unittest.TestCase):
    def test_core_services_exist(self):
        files = [
            'backend/app/services/face_shape_service.py',
            'backend/app/services/hairstyle_service.py',
            'backend/app/services/hair_health_service.py',
            'backend/app/services/appointment_service.py',
            'backend/app/services/email_service.py',
        ]
        for file in files:
            with self.subTest(file=file):
                self.assertTrue(Path(file).exists())
