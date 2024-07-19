#!/usr/bin/python3
import unittest
from models.amenity import Amenity
""" TestAmenity Class """


class TestAmenity(unittest.TestCase):
    """ Test for the Amenity Class """
    def setUp(self):
        self.a = Amenity()

    def test_classname(self):
        self.assertEqual(self.a.to_dict()['__class__'], 'Amenity')


if __name__ == "__main__":
    unittest.main()
