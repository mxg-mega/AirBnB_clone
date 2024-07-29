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

    def test_email(self):
        self.a.email = 'airbnb@gmail.com'
        self.a.password = 'bnb1'
        self.a.first_name = 'air'
        self.a.last_name = 'bnb'
        self.assertEqual(self.a.to_dict()['email'], 'airbnb@gmail.com')
        self.assertEqual(self.a.to_dict()['password'], 'bnb1')
        self.assertEqual(self.a.to_dict()['first_name'], 'air')
        self.assertEqual(self.a.to_dict()['last_name'], 'bnb')


if __name__ == "__main__":
    unittest.main()
