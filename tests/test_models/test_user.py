#!/usr/bin/python3
"""Defines unittests for models/user.py."""

import unittest
from models.user import User
from models.base_model import BaseModel
from datetime import datetime


class TestUser(unittest.TestCase):
    """ Test for the User Class """
    def setUp(self):
        """Set up test methods."""
        self.user = User()

    def test_is_instance_of_base_model(self):
        """Test if User is instance of BaseModel."""
        self.assertIsInstance(self.user, BaseModel)

    def test_attributes_exist(self):
        """Test if User has the correct attributes."""
        self.assertTrue(hasattr(self.user, "email"))
        self.assertTrue(hasattr(self.user, "password"))
        self.assertTrue(hasattr(self.user, "first_name"))
        self.assertTrue(hasattr(self.user, "last_name"))

    def test_attributes_default_values(self):
        """Test the default values of User attributes."""
        self.assertEqual(self.user.email, "")
        self.assertEqual(self.user.password, "")
        self.assertEqual(self.user.first_name, "")
        self.assertEqual(self.user.last_name, "")

    def test_set_attributes(self):
        """Test setting attributes of User."""
        self.user.email = "user@example.com"
        self.user.password = "password"
        self.user.first_name = "First"
        self.user.last_name = "Last"
        self.assertEqual(self.user.email, "user@example.com")
        self.assertEqual(self.user.password, "password")
        self.assertEqual(self.user.first_name, "First")
        self.assertEqual(self.user.last_name, "Last")

    def test_to_dict_contains_correct_keys(self):
        """Test if to_dict contains correct keys."""
        user_dict = self.user.to_dict()
        self.assertIn("id", user_dict)
        self.assertIn("created_at", user_dict)
        self.assertIn("updated_at", user_dict)
        self.assertIn("__class__", user_dict)
        self.assertIn("email", user_dict)
        self.assertIn("password", user_dict)
        self.assertIn("first_name", user_dict)
        self.assertIn("last_name", user_dict)

    def test_to_dict_contains_correct_values(self):
        """Test if to_dict contains correct values."""
        self.user.email = "user@example.com"
        self.user.password = "password"
        self.user.first_name = "First"
        self.user.last_name = "Last"
        user_dict = self.user.to_dict()
        self.assertEqual(user_dict["email"], "user@example.com")
        self.assertEqual(user_dict["password"], "password")
        self.assertEqual(user_dict["first_name"], "First")
        self.assertEqual(user_dict["last_name"], "Last")

    def test_created_at_is_datetime(self):
        """Test if created_at is a datetime object."""
        self.assertIsInstance(self.user.created_at, datetime)

    def test_updated_at_is_datetime(self):
        """Test if updated_at is a datetime object."""
        self.assertIsInstance(self.user.updated_at, datetime)

    def test_str_representation(self):
        """Test the string representation of User."""
        self.user.email = "user@example.com"
        string = "[User] ({}) {}".format(self.user.id, self.user.__dict__)
        self.assertEqual(str(self.user), string)


if __name__ == "__main__":
    unittest.main()
