import unittest
from models.state import State

class TestState(unittest.TestCase):

    def test_init(self):
        """Test for correct initialization of State"""
        state = State()
        self.assertTrue(hasattr(state, "name"))
        self.assertEqual(state.name, "")

    def test_save(self):
        """Test the save method of the State class"""
        state = State()
        state.save()
        self.assertTrue(state.id)
        self.assertTrue(state.updated_at)

if __name__ == '__main__':
    unittest.main()

