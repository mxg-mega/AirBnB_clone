#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
""" TestBaseModel Class """


class TestBaseModel(unittest.TestCase):
    """ Test for the BaseModel Class """
    def test_classname(self):
        a = BaseModel()
        self.assertEqual(a.to_dict()['class'], 'BaseModel')

if __name__ == "__main__":
    unittest.main()
