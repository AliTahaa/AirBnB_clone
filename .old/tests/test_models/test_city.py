#!/usr/bin/python3
"""
Test city class
"""


import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """ test for city """
    def setUp(self):
        """ standard setUp() """
        self.model = City()

    def test_public_attr(self):
        """ public attribute exists and if equal to empty string """
        self.assertTrue(hasattr(self.model, "state_id"))
        self.assertTrue(hasattr(self.model, "name"))
        self.assertEqual(self.model.state_id, "")
        self.assertEqual(self.model.name, "")

    def test_strings(self):
        """ input for each attr """
        self.model.name = "cairo"
        self.model.state_id = "13fe4e9f-8b94-4dd2-af31-8db9180aa3f4"
        self.assertEqual(self.model.name, "cairo")
        self.assertEqual(self.model.state_id,
                         "13fe4e9f-8b94-4dd2-af31-8db9180aa3f4")


if __name__ == '__main__':
    unittest.main()
