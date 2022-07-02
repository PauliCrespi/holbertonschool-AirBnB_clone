#!/usr/bin/env python3

import unittest
from models.user import User
from models.base_model import BaseModel


class testUser(unittest.TestCase):
    """tests for user"""

    def test1(self):
        """checks attributes"""
        user = User()
        self.assertTrue(hasattr(user, "email"))
        self.assertTrue(hasattr(user, "password"))
        self.assertTrue(hasattr(user, "first_name"))
        self.assertTrue(hasattr(user, "last_name"))

