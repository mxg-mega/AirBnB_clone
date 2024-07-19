#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
""" TestBaseModel Class """


class TestBaseModel(unittest.TestCase):
    """ Test for the BaseModel Class """

    def setUp(self):
        self.a = BaseModel()

    def test_classname(self):
        self.assertEqual(self.a.to_dict()['class'], 'BaseModel')

    def test_id(self):
        self.assertIsNotNone(self.a.id)

if __name__ == "__main__":
    unittest.main()
