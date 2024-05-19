#!/usr/bin/python3
""" Test place class """


import unittest
from datetime import datetime
from models.place import Place


class TestPlace(unittest.TestCase):
    """ test for place """
    def setUp(self):
        """ standard setUp() """
        self.model = Place()
        self.model.save()

    def test_public_attr(self):
        """ if public attribute exists and if equal to
        empty string int or float
        """
        self.assertTrue(hasattr(self.model, "city_id"))
        self.assertTrue(hasattr(self.model, "user_id"))
        self.assertTrue(hasattr(self.model, "name"))
        self.assertTrue(hasattr(self.model, "description"))
        self.assertTrue(hasattr(self.model, "number_rooms"))
        self.assertTrue(hasattr(self.model, "number_bathrooms"))
        self.assertTrue(hasattr(self.model, "max_guest"))
        self.assertTrue(hasattr(self.model, "price_by_night"))
        self.assertTrue(hasattr(self.model, "latitude"))
        self.assertTrue(hasattr(self.model, "longitude"))
        self.assertTrue(hasattr(self.model, "amenity_ids"))
        self.assertEqual(self.model.city_id, "")
        self.assertEqual(self.model.user_id, "")
        self.assertEqual(self.model.name, "")
        self.assertEqual(self.model.description, "")
        self.assertEqual(self.model.number_rooms, 0)
        self.assertEqual(self.model.number_bathrooms, 0)
        self.assertEqual(self.model.max_guest, 0)
        self.assertEqual(self.model.price_by_night, 0)
        self.assertEqual(self.model.latitude, 0.0)
        self.assertEqual(self.model.longitude, 0.0)
        self.assertEqual(self.model.amenity_ids, [])

    def test_string_int_float(self):
        """ input for each attr """
        self.model.city_id = 33
        self.model.user_id = 23
        self.model.name = "flky"
        self.model.description = "very good room"
        self.model.number_rooms = 3
        self.model.number_bathrooms = 2
        self.model.max_guest = 6
        self.model.price_by_night = 300
        self.model.latitude = 2.1
        self.model.longitude = 2.3
        self.model.amenity_ids = ['4321', '54321']
        self.assertEqual(self.model.city_id, 33)
        self.assertEqual(self.model.user_id, 23)
        self.assertEqual(self.model.name, "flky")
        self.assertEqual(self.model.description, "very good room")
        self.assertEqual(self.model.number_rooms, 3)
        self.assertEqual(self.model.number_bathrooms, 2)
        self.assertEqual(self.model.max_guest, 6)
        self.assertEqual(self.model.price_by_night, 300)
        self.assertEqual(self.model.latitude, 2.1)
        self.assertEqual(self.model.longitude, 2.3)
        self.assertEqual(self.model.amenity_ids, ['4321', '54321'])


if __name__ == '__main__':
    unittest.main()
