#!/usr/bin/python3
import unittest
from models.state import State
""" TestState Class """


class TestState(unittest.TestCase):
    """ Test for the BaseModel Class """

    def setUp(self):
        self.a = State()

    def test_classname(self):
        self.assertEqual(self.a.to_dict()['__class__'], 'State')

if __name__ == "__main__":
    unittest.main()
