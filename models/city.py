import unittest
from models.city import City

class TestCity(unittest.TestCase):
    
    def test_init(self):
        """Test for correct initialization of City"""
        city = City()
        self.assertTrue(hasattr(city, "state_id"))
        self.assertTrue(hasattr(city, "name"))
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

    def test_save(self):
        """Test the save method of the City class"""
        city = City()
        city.save()
        self.assertTrue(city.id)
        self.assertTrue(city.updated_at)

if __name__ == '__main__':
    unittest.main()


