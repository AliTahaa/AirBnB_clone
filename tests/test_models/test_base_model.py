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
        self.assertNotEqual(self.model1.created_at, self.model2.updated_at)


if __name__ == "__main__":
    unittest.main()
