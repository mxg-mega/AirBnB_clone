#!/usr/bin/python3
import unittest
from models.place import Place
""" TestPlace Class """


class TestPlace(unittest.TestCase):
    """ Test for the Place Class """

    def test_classname(self):
        a = Place()
        self.assertEqual(a.to_dict()['class'], 'Place')

if __name__ == "__main__":
    unittest.main()
