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

    def test2(self):
        """checks if attributes are empty"""
        usr = User()
        self.assertEqual(usr.email, "")
        self.assertEqual(usr.password, "")
        self.assertEqual(usr.first_name, "")
        self.assertEqual(usr.last_name, "")

    def test3(self):
        """checks attributes types"""
        usr = User()
        self.asserEqual(type(usr.email), str)
        self.asserEqual(type(usr.password), str)
        self.asserEqual(type(usr.first_name), str)
        self.asserEqual(type(usr.last_name), str)
