#!/usr/bin/python3
""" Unitest for base_model """
import unittest
from models.base_model import BaseModel

bm = BaseModel()


class TestBaseModel(unittest.TestCase):
    """tests"""

    def test0(self):
        """tests name"""
        x = BaseModel()
        x.name = "myModel"
        self.assertEqual(x.name, "myModel")

    def test1(self):
        """tests save function"""
        y = BaseModel()
        created_at_i = y.created_at
        updated_at_i = y.updated_at
        y.save()
        created_at_j = y.created_at
        updated_at_j = y.updated_at
        self.assertEqual(created_at_i, created_at_j)
        self.assertNotEqual(updated_at_i, updated_at_j)

    def test2(self):
        """tests to_dict function"""
        bm.my_number = 11
        bm.name = "model"
        bm_d = bm.to_dict()
        key = ["id", "name", "my_number", "created_at",
               "updated_at", "__class__"]
        self.assertCountEqual(bm_d.keys(), key)
        self.assertEqual(bm_d["__class__"], "BaseModel")
        self.assertEqual(bm_d["my_number"], 11)
        self.assertEqual(bm_d["name"], "model")

    def test3(self):
        """tests str"""
        s = f"[{type(bm).__name__}] ({bm.id}) {bm.__dict__}"
        self.assertEqual(s, str(bm))


if __name__ == '__main__':
    unittest.main()
