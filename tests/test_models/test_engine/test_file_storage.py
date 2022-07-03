#!/usr/bin/env python3

import unittest
import models
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class TestFileStorage(unittest.TestCase):
    """tests for file storage"""

    def test1(self):
        """test type"""
        x = FileStorage()
        self.assertEqual(type(x.all()), dict)


if __name__ == '__main__':
    unittest.main()
