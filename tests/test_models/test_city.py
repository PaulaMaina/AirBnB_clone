#!/usr/bin/python3
"""Test cases for the City class"""
from models.base_model import BaseModel
from models.city import City
import unittest


class TestCity(unittest.TestCase):
    """A TestCase for the City class"""
    def test_inherits_BaseModel(self):
        """Tests if City class inherits from BaseModel class"""
        instance = City()
        self.assertIsInstance(instance, BaseModel)

    def test_state_id_exists(self):
        """Tests the default state_id value"""
        self.assertEqual(hasattr(City, "state_id"), True)
        self.assertIs(type(City.state_id), str)
        self.assertEqual(City.state_id, "")

    def test_name_exists(self):
        """Tests the default name value"""
        self.assertEqual(hasattr(City, "name"), True)
        self.assertIs(type(City.name), str)
        self.assertEqual(City.name, "")
