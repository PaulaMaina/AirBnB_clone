#!/usr/bin/python3
"""Test cases for the Place class"""
from models.base_model import BaseModel
from models.place import Place
import unittest


class TestPlace(unittest.TestCase):
    """A TestCase for the Place class"""
    def test_inherits_BaseModel(self):
        """Tests if Place class inherits from BaseModel class"""
        instance = Place()
        self.assertIsInstance(instance, BaseModel)

    def test_city_id_exists(self):
        """Tests the default city_id value"""
        self.assertEqual(hasattr(Place, "city_id"), True)
        self.assertIs(type(Place.city_id), str)
        self.assertEqual(Place.city_id, "")

    def test_user_id_exists(self):
        """Tests the default city_id value"""
        self.assertEqual(hasattr(Place, "user_id"), True)
        self.assertIs(type(Place.user_id), str)
        self.assertEqual(Place.user_id, "")

    def test_name_exists(self):
        """Tests the default name value"""
        self.assertEqual(hasattr(Place, "name"), True)
        self.assertIs(type(Place.name), str)
        self.assertEqual(Place.name, "")

    def test_description_exists(self):
        """Tests the default description value"""
        self.assertEqual(hasattr(Place, "description"), True)
        self.assertIs(type(Place.description), str)
        self.assertEqual(Place.description, "")

    def test_number_rooms_exists(self):
        """Tests the default number_rooms value"""
        self.assertEqual(hasattr(Place, "number_rooms"), True)
        self.assertIs(type(Place.number_rooms), int)
        self.assertEqual(Place.number_rooms, 0)

    def test_number_bathrooms_exists(self):
        """Tests the default number_bathrooms value"""
        self.assertEqual(hasattr(Place, "number_bathrooms"), True)
        self.assertIs(type(Place.number_bathrooms), int)
        self.assertEqual(Place.number_bathrooms, 0)

    def test_max_guest_exists(self):
        """Tests the default max_guest value"""
        self.assertEqual(hasattr(Place, "max_guest"), True)
        self.assertIs(type(Place.max_guest), int)
        self.assertEqual(Place.max_guest, 0)

    def test_price_by_night_exists(self):
        """Tests the default price_by_night value"""
        self.assertEqual(hasattr(Place, "price_by_night"), True)
        self.assertIs(type(Place.price_by_night), int)
        self.assertEqual(Place.price_by_night, 0)

    def test_latitude_exists(self):
        """Tests the default latitude value"""
        self.assertEqual(hasattr(Place, "latitude"), True)
        self.assertIs(type(Place.latitude), float)
        self.assertEqual(Place.latitude, 0)

    def test_longitude_exists(self):
        """Tests the default longitude value"""
        self.assertEqual(hasattr(Place, "longitude"), True)
        self.assertIs(type(Place.longitude), float)
        self.assertEqual(Place.longitude, 0)

    def test_amenity_ids_exists(self):
        """Tests the default amenity_ids value"""
        self.assertEqual(hasattr(Place, "amenity_ids"), True)
        self.assertIs(type(Place.amenity_ids), list)
        self.assertEqual(Place.amenity_ids, [])
