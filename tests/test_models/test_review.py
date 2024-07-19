#!/usr/bin/python3
import unittest
from models.review import Review
""" TestReview Class """


class TestReview(unittest.TestCase):
    """ Test for the Review Class """

    def test_classname(self):
        a = Review()
        self.assertEqual(a.to_dict()['class'], 'Review')

if __name__ == "__main__":
    unittest.main()
