import unittest
from models.review import Review

class TestReview(unittest.TestCase):

    def test_init(self):
        """Test for correct initialization of Review"""
        review = Review()
        self.assertTrue(hasattr(review, "place_id"))
        self.assertTrue(hasattr(review, "user_id"))
        self.assertTrue(hasattr(review, "text"))
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")

    def test_save(self):
        """Test the save method of the Review class"""
        review = Review()
        review.save()
        self.assertTrue(review.id)
        self.assertTrue(review.updated_at)

if __name__ == '__main__':
    unittest.main()

