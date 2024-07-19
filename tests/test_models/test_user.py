#!/usr/bin/python3
import unittest
from models.user import User
""" TestUser Class """


class TestUser(unittest.TestCase):
    """ Test for the User Class """
    def test_classname(self):
        a = User()
        self.assertEqual(a.to_dict()['class'], 'User')


if __name__ == "__main__":
    unittest.main()
