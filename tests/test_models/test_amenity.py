#!/usr/bin/python3
import unittest
from models.amenity import Amenity
""" TestAmenity Class """


class TestAmenity(unittest.TestCase):
    """ Test for the Amenity Class """
    def setUp(self):
       """Set up test methods."""
        self.amenity = Amenity()

    def test_attributes_exist(self):
        """Test if Amenity has the correct attributes."""
        self.assertTrue(hasattr(self.amenity, "name"))

    def test_attributes_default_values(self):
        """Test the default values of Amenity attributes."""
        self.assertEqual(self.amenity.name, "")


if __name__ == "__main__":
    unittest.main()
