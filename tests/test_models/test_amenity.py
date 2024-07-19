#!/usr/bin/python3
import unittest
from models.amenity import Amenity
""" TestAmenity Class """


class TestAmenity(unittest.TestCase):
    """ Test for the Amenity Class """
    def test_classname(self):
        a = Amenity()
        self.assertEqual(a.to_dict()['class'], 'Amenity')

if __name__ == "__main__":
    unittest.main()
