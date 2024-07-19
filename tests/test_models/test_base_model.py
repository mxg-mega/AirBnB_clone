#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
""" TestBaseModel Class """


class TestBaseModel(unittest.TestCase):
    """ Test for the BaseModel Class """

    def setUp(self):
        a = BaseModel()

    def test_classname(self):
        self.assertEqual(a.to_dict()['class'], 'BaseModel')

    def test_id(self):
        self.assertNotNone

if __name__ == "__main__":
    unittest.main()
