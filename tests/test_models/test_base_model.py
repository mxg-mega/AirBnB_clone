#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
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
        prev = self.a.updated_at
        self.a.save()
        self.assertNotEqual(prev, self.a.updated_at)

    def test_str(self):
        self.assertEqual(self.a.__str__(), "[{}] ({}) {}".format(self.a.to_dict()['__class__'],
                         self.a.id, self.a.__dict__))

if __name__ == "__main__":
    unittest.main()
