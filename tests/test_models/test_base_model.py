#!/usr/bin/env python3
import unittest
import path_setup
from models.base_model import BaseModel
from datetime import datetime
""" TestBaseModel Class """


class TestBaseModel(unittest.TestCase):
    """ Test for the BaseModel Class """
    def test_classinstance(self):
        b = BaseModel()
        self.assertEqual(BaseModel().nb_instances, 2)

if __name__ == "__main__":
    unittest.main()
