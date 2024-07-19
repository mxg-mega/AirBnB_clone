#!/usr/bin/python3
import unittest
from models.city import City
""" TestCity class """


class TestCity(unittest.TestCase):
    """ Tests for City class """

    def test_classname(self):
        a = City()
        self.assertEqual(a.to_dict()['class'], 'City')
