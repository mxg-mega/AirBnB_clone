#!/usr/bin/python3
import unittest
from models.city import City
""" TestCity class """


class TestCity(unittest.TestCase):
    """ Tests for City class """

    def setUp(self):
        self.a = City()

    def test_classname(self):
        self.assertEqual(self.a.to_dict()['__class__'], 'City')


if __name__ == '__main__':
    unittest.main()
