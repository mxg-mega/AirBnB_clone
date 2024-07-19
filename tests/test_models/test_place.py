#!/usr/bin/python3
import unittest
from models.place import Place
""" TestPlace Class """


class TestPlace(unittest.TestCase):
    """ Test for the Place Class """

    def setUp(self):
        self.a = Place()

    def test_classname(self):
        self.assertEqual(self.a.to_dict()['__class__'], 'Place')


if __name__ == "__main__":
    unittest.main()
