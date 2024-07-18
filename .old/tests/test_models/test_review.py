#!/usr/bin/python3
""" Test review class """


import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """ test for review """
    def setUp(self):
        """ standard setUp() """
        self.model = Review()

    def test_public_attr(self):
        """ if public attribute exists and if equal to empty string """
        self.assertTrue(hasattr(self.model, "place_id"))
        self.assertTrue(hasattr(self.model, "user_id"))
        self.assertTrue(hasattr(self.model, "text"))
        self.assertEqual(self.model.place_id, "")
        self.assertEqual(self.model.user_id, "")
        self.assertEqual(self.model.text, "")

    def test_strings(self):
        """ input for each attr """
        self.model.place_id = 33
        self.model.user_id = 66
        self.model.text = "hmmm"
        self.assertEqual(self.model.place_id, 33)
        self.assertEqual(self.model.user_id, 66)
        self.assertEqual(self.model.text, "hmmm")


if __name__ == '__main__':
    unittest.main()
