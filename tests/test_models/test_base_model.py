#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
import datetime
from uuid import UUID
import json
import os

""" TestBaseModel Class """


class TestBaseModel(unittest.TestCase):
    """ Test for the BaseModel Class """

    def setUp(self):
        self.a = BaseModel()

    def test_classname(self):
        self.assertEqual(self.a.to_dict()['__class__'], 'BaseModel')

    def test_id(self):
        self.assertIsNotNone(self.a.id)

    def test_save(self):
         """ Testing save """
         self.a.save()
         key = self.a.to_dict()["__class__"] + "." + self.a.to_dict()['id']
         with open('file.json', 'r') as f:
             j = json.load(f)
             self.assertEqual(j[key], self.a.to_dict())

    def test_str(self):
        self.assertEqual(self.a.__str__(), "[{}] ({}) {}".format(self.a.to_dict()['__class__'],
                         self.a.id, self.a.__dict__))



if __name__ == "__main__":
    unittest.main()
