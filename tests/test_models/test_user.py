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
        User.email = 'airbnb@gmail.com'
        User.password = 'bnb1'
        User.first_name = 'air'
        User.last_name = 'bnb'
        self.assertEqual(User.email, 'airbnb@gmail.com')
        self.assertEqual(User.password, 'bnb1')
        self.assertEqual(User.first_name, 'air')
        self.assertEqual(User.last_name, 'bnb')


if __name__ == "__main__":
    unittest.main()
