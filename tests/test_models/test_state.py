#!/usr/bin/python3
import unittest
from models.state import State
""" TestState Class """


class TestState(unittest.TestCase):
    """ Test for the BaseModel Class """

   def setUp(self):
        """Set up test methods."""
        self.state = State()

    def test_attributes_exist(self):
        """Test if State has the correct attributes."""
        self.assertTrue(hasattr(self.state, "name"))

    def test_attributes_default_values(self):
        """Test the default values of State attributes."""
        self.assertEqual(self.state.name, "") 

if __name__ == "__main__":
    unittest.main()
