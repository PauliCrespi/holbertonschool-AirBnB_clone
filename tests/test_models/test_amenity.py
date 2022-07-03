#!/usr/bin/env python3

import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class testAmenity(unittest.TestCase):
    """tests for Amenity"""

    def test1(self):
        """tests name"""
        am = Amenity()
        self.assertEqual(am.name, "")


if __name__ == '__main__':
    unittest.main()
