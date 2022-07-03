#!/usr/bin/env python3


import unittest
from models.place import Place
from models.base_model import BaseModel


class testPlace(unittest.TestCase):
    """tests for Place"""

    def test1(self):
        """tests for everything in Place"""
        place = Place()
        self.assertEqual(place.city_id, "")
        self.assertEqual(place.user_id, "")
        self.assertEqual(place.name, "")
        self.assertEqual(place.description, "")
        self.assertEqual(place.number_rooms, "")
        self.assertEqual(place.number_bathrooms, "")
        self.assertEqual(place.max_guest, "")
        self.assertEqual(place.price_by_night, "")
        self.assertEqual(place.latitude, "")
        self.assertEqual(place.longitude, "")
        self.assertEqual(place.amenity_ids, "")


if __name__ == '__main__':
    unittest.main()
