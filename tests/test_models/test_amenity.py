#!/usr/bin/python3
"""Test cases for the Amenity class"""
from models.amenity import Amenity
from models.base_model import BaseModel
import unittest


class TestAmenity(unittest.TestCase):
    """A TestCase for the Amenity class"""
    def test_inherits_BaseModel(self):
        """Tests if Amenity class inherits from BaseModel"""
        instance = Amenity()
        self.assertIsInstance(instance, BaseModel)

    def test_name_exists(self):
        """Tests the default name value"""
        self.assertEqual(hasattr(Amenity, "name"), True)
        self.assertIs(type(Amenity.name), str)
        self.assertEqual(Amenity.name, "")
