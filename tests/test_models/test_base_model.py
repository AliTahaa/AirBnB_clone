#!/usr/bin/python3
"""Unittest for BaseModel class"""

import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test Base model"""
    def setUp(self):
        self.model1 = BaseModel()

    def test_attr(self):
        self.assertTrue(getattr(self.model1, "id"))


if __name__ == "__main__":
    unittest.main()
