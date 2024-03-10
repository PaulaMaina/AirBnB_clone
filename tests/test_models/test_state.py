#!/usr/bin/python3
"""Test cases for the State class"""
from models.base_model import BaseModel
from models.state import State
import unittest


class TestState(unittest.TestCase):
    """A TestCase for the State class"""
    def test_inherits_BaseModel(self):
        """Tests if State class inherits from BaseModel class"""
        instance = State()
        self.assertIsInstance(instance, BaseModel)

    def test_name_exists(self):
        """Tests the default name value"""
        self.assertEqual(hasattr(State, "name"), True)
        self.assertIs(type(State.name), str)
        self.assertEqual(State.name, "")
