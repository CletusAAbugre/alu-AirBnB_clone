import unittest
from models.base_model import BaseModel
from datetime import datetime

class TestBaseModel(unittest.TestCase):
    
    def test_init(self):
        """Test for correct initialization of BaseModel"""
        obj = BaseModel()
        self.assertTrue(hasattr(obj, "id"))
        self.assertTrue(hasattr(obj, "created_at"))
        self.assertTrue(hasattr(obj, "updated_at"))
    
    def test_to_dict(self):
        """Test if to_dict method returns a dictionary"""
        obj = BaseModel()
        obj_dict = obj.to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertTrue("id" in obj_dict)
        self.assertTrue("created_at" in obj_dict)
        self.assertTrue("updated_at" in obj_dict)
    
    def test_str(self):
        """Test the string representation"""
        obj = BaseModel()
        obj_str = str(obj)
        self.assertIn("[BaseModel]", obj_str)
        self.assertIn(f"({obj.id})", obj_str)

if __name__ == "__main__":
    unittest.main()

