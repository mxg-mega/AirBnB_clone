#!/usr/bin/python3
import unittest
from models.review import Review
""" TestReview Class """


class TestReview(unittest.TestCase):
    """ Test for the Review Class """

    def setUp(self):
        self.a = Review()

    def test_classname(self):
        self.assertEqual(self.a.to_dict()['__class__'], 'Review')


if __name__ == "__main__":
    unittest.main()
