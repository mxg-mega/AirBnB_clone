#!/usr/bin/python3
import unittest
from models.state import State
""" TestState Class """


class TestState(unittest.TestCase):
    """ Test for the BaseModel Class """

    def test_classname(self):
        a = State()
        self.assertEqual(a.to_dict()['class'], 'State')

if __name__ == "__main__":
    unittest.main()
