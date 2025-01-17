import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    def test_initialization(self):
        obj = BaseModel()
        self.assertTrue(hasattr(obj, "id"))
        self.assertTrue(hasattr(obj, "created_at"))

if __name__ == "__main__":
    unittest.main()

