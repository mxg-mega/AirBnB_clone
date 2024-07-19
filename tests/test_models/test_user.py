#!/usr/bin/python3
import unittest
from models.user import User
""" TestUser Class """


class TestUser(unittest.TestCase):
    """ Test for the User Class """
    def setUp(self):
        self.a = User()

    def test_classname(self):
        self.assertEqual(self.a.to_dict()['__class__'], 'User')


if __name__ == "__main__":
    unittest.main()
