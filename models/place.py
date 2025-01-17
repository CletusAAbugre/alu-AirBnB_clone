import unittest
from models.place import Place

class TestPlace(unittest.TestCase):

    def test_init(self):
        """Test for correct initialization of Place"""
        place = Place()
        self.assertTrue(hasattr(place, "city_id"))
        self.assertTrue(hasattr(place, "user_id"))
        self.assertTrue(hasattr(place, "name"))
        self.assertEqual(place.city_id, "")
        self.assertEqual(place.user_id, "")
        self.assertEqual(place.name, "")
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(place.latitude, 0.0)
        self.assertEqual(place.longitude, 0.0)
        self.assertEqual(place.amenity_ids, [])

    def test_save(self):
        """Test the save method of the Place class"""
        place = Place()
        place.save()
        self.assertTrue(place.id)
        self.assertTrue(place.updated_at)

if __name__ == '__main__':
    unittest.main()

