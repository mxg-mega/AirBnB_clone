#!/usr/bin/python3
import unittest
from models.engine.file_storage import FileStorage
""" TestFileStorage Class """


class TestFileStorage(unittest.TestCase):
    """ Tests for the FileStorage class """

    def test_classname(self):
        a = FileStorage()
        self.assertEqual(a.to_dict()['class'], 'FileStorage')


if __name__ == '__main__':
    unittest.main()
