from pathlib import Path
import unittest


class TestProjectScaffoldIntegration(unittest.TestCase):
    def test_backend_frontend_deployment_directories_exist(self):
        for path in ['backend', 'frontend', 'deployment', 'docs', 'tests', 'datasets']:
            with self.subTest(path=path):
                self.assertTrue(Path(path).exists())
