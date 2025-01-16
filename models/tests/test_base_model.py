import unittest
from models.base_model import BaseModel
from models import storage

class TestBaseModel(unittest.TestCase):
    def test_instance_creation(self):
        obj = BaseModel()
        self.assertTrue(isinstance(obj, BaseModel))

    def test_to_dict(self):
        obj = BaseModel()
        dict_repr = obj.to_dict()
        self.assertIn("id", dict_repr)
        self.assertIn("created_at", dict_repr)
        self.assertIn("updated_at", dict_repr)
        self.assertIn("__class__", dict_repr)

    def test_save(self):
        obj = BaseModel()
        obj.save()
        self.assertTrue(len(storage.all()) > 0)

    def test_reload(self):
        obj = BaseModel()
        obj.save()
        storage.reload()
        self.assertIn(f"BaseModel.{obj.id}", storage.all())

if __name__ == '__main__':
    unittest.main()

