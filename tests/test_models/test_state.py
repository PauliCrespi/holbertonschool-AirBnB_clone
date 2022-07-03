#!/usr/bin/env python3


import unittest
from models.state import State
from models.base_model import BaseModel


class testState(unittest.TestCase):
    """tests for State"""

    def test1(self):
        """tests state name and save"""
        state = State()
        self.assertEqual(state.name, "")


if __name__ == '__main__':
    unittest.main()
