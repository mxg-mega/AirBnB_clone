#!/usr/bin/python3
import unittest
from models.review import Review
""" TestReview Class """


class TestReview(unittest.TestCase):
    """ Test for the Review Class """

    def setUp(self):
        """Set up test methods."""
        self.review = Review()

    def test_attributes_exist(self):
        """Test if Review has the correct attributes."""
        self.assertTrue(hasattr(self.review, "place_id"))
        self.assertTrue(hasattr(self.review, "user_id"))
        self.assertTrue(hasattr(self.review, "text"))

    def test_attributes_default_values(self):
        """Test the default values of Review attributes."""
        self.assertEqual(self.review.place_id, "")
        self.assertEqual(self.review.user_id, "")
        self.assertEqual(self.review.text, "")


if __name__ == "__main__":
    unittest.main()
