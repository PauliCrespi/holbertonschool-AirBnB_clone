#!/usr/bin/env python3


import unittest
from models.review import Review
from models.base_model import BaseModel


class testReview(unittest.TestCase):
    """tests for Review"""

    def test1(self):
        """tests place_id, user_id and text"""
        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")


if __name__ == '__main__':
    unittest.main()
