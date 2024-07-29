#!/usr/bin/python3
import unittest
from models.city import City
""" TestCity class """


class TestCity(unittest.TestCase):
    """ Tests for City class """

   def setUp(self):
        """Set up test methods."""
        self.city = City()

    def test_attributes_exist(self):
        """Test if City has the correct attributes."""
        self.assertTrue(hasattr(self.city, "state_id"))
        self.assertTrue(hasattr(self.city, "name"))

    def test_attributes_default_values(self):
        """Test the default values of City attributes."""
        self.assertEqual(self.city.state_id, "")
        self.assertEqual(self.city.name, "") 


if __name__ == '__main__':
    unittest.main()
