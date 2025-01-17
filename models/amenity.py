import unittest
from models.amenity import Amenity

class TestAmenity(unittest.TestCase):

    def test_init(self):
        """Test for correct initialization of Amenity"""
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, "name"))
        self.assertEqual(amenity.name, "")

    def test_save(self):
        """Test the save method of the Amenity class"""
        amenity = Amenity()
        amenity.save()
        self.assertTrue(amenity.id)
        self.assertTrue(amenity.updated_at)

if __name__ == '__main__':
    unittest.main()

