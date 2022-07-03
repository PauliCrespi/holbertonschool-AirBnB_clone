#!/usr/bin/env python3

import unittest
from models.city import City
from models.base_model import BaseModel


class testCity(unittest.TestCase):
    """tests for city"""

    def test1(self):
        """tests state_id and name"""
        city = City()
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")


if __name__ == '__main__':
    unittest.main()
