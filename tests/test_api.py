import importlib.util
from pathlib import Path
import unittest


class TestApiScaffold(unittest.TestCase):
    def test_main_file_exists(self):
        path = Path('backend/app/main.py')
        self.assertTrue(path.exists())

    def test_main_defines_app_symbol(self):
        content = Path('backend/app/main.py').read_text(encoding='utf-8')
        self.assertIn('app = FastAPI', content)

    def test_main_module_is_syntax_valid(self):
        spec = importlib.util.spec_from_file_location('main', 'backend/app/main.py')
        self.assertIsNotNone(spec)
