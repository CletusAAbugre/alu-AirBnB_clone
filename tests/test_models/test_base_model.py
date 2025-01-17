import unittest
from datetime import datetime
from models.base_model import BaseModel  # Adjust the import path if necessary

class TestBaseModel(unittest.TestCase):

    def test_instance_creation(self):
        obj = BaseModel()
        self.assertIsInstance(obj, BaseModel)
        self.assertTrue(isinstance(obj.id, str))  # Check id type
        self.assertTrue(isinstance(obj.created_at, datetime))  # Check created_at type
        self.assertTrue(isinstance(obj.updated_at, datetime))  # Check updated_at type

    def test_str_method(self):
        obj = BaseModel()
        str_repr = f"[BaseModel] ({obj.id}) {{'id': '{obj.id}', 'created_at': '{obj.created_at.isoformat()}', 'updated_at': '{obj.updated_at.isoformat()}'}}"
        self.assertEqual(str(obj), str_repr)

    def test_to_dict_method(self):
        obj = BaseModel()
        obj_dict = obj.to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertEqual(obj_dict['__class__'], 'BaseModel')
        self.assertTrue('created_at' in obj_dict)
        self.assertTrue('updated_at' in obj_dict)

    def test_save_method(self):
        obj = BaseModel()
        original_updated_at = obj.updated_at
        obj.save()
        self.assertNotEqual(original_updated_at, obj.updated_at)

if __name__ == '__main__':
    unittest.main()

