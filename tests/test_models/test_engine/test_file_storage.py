#!/usr/bin/python3
import unittest
from models.engine.file_storage import FileStorage
""" TestFileStorage Class """


class TestFileStorage(unittest.TestCase):
    """ Tests for the FileStorage class """

    def setUp(self):
        self.a = FileStorage()

    def test_classname(self):
        self.assertEqual(self.a.to_dict()['__class__'], 'FileStorage')



if __name__ == '__main__':
    unittest.main()
