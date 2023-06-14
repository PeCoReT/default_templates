import unittest
import yaml
from pathlib import Path


class MissingCategoryTestCase(unittest.TestCase):
    def test_missing_category(self):
        vulnerability_templates_path = Path(__file__).parent.parent / "vulnerability_templates"
        category_path = vulnerability_templates_path / "categories.yaml"
        with open(category_path, "r") as f:
            categories = list(yaml.safe_load(f).keys())
        for path in vulnerability_templates_path.rglob("info.yaml"):
            with open(path, "r") as f:
                for item in yaml.safe_load(f):
                    self.assertIn(item["category"], categories)
