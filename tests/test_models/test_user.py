#!/usr/bin/python
""" Test user class """
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """test for user"""
    def setUp(self):
        """ standard setUp() """
        self.model = User()

    def test_public_attr(self):
        """ if public attributes are exist and if equal to empty string """
        self.assertTrue(hasattr(self.model, "email"))
        self.assertTrue(hasattr(self.model, "password"))
        self.assertTrue(hasattr(self.model, "first_name"))
        self.assertTrue(hasattr(self.model, "last_name"))
        self.assertEqual(self.model.email, "")
        self.assertEqual(self.model.password, "")
        self.assertEqual(self.model.first_name, "")
        self.assertEqual(self.model.last_name, "")

    def test_strings(self):
        """ input for each attr """
        self.model.email = "haha@cool.com"
        self.model.password = "hjhjhj"
        self.model.first_name = "hasan"
        self.model.last_name = "mohamed"
        self.assertEqual(self.model.email, "haha@cool.com")
        self.assertEqual(self.model.password, "hjhjhj")
        self.assertEqual(self.model.first_name, "hasan")
        self.assertEqual(self.model.last_name, "mohamed")


if __name__ == '__main__':
    unittest.main()
