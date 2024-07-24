#!/usr/bin/python3
"""Unittest for BaseModel class"""

import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test Base model"""
    def setUp(self):
        self.model1 = BaseModel()
        self.model2 = BaseModel()

    def test_attr(self):
        self.assertNotEqual(self.model1.id, self.model2.id)

    def test_save(self):
        first_time = self.model1.updated_at
        self.model1.save()
        self.assertNotEqual(first_time, self.model1.updated_at)

    def test_to_dect(self):
        dic = self.model1.to_dict()
        self.assertEqual(dic["__class__"], self.__class__.__name__)



if __name__ == "__main__":
    unittest.main()
