#!/usr/bin/python3
"""Test cases for the User class"""
from models.base_model import BaseModel
from models.user import User
import unittest


class TestUser(unittest.TestCase):
    """A TestCase for the User class"""
    def test_inherits_BaseModel(self):
        """Tests if User class inherits from BaseModel class"""
        instance = User()
        self.assertIsInstance(instance, BaseModel)

    def test_email_exists(self):
        """Tests the default email value"""
        self.assertEqual(hasattr(User, "email"), True)
        self.assertIs(type(User.email), str)
        self.assertEqual(User.email, "")

    def test_password_exists(self):
        """Tests the default password value"""
        self.assertEqual(hasattr(User, "password"), True)
        self.assertIs(type(User.password), str)
        self.assertEqual(User.password, "")

    def test_first_name_exists(self):
        """Tests the default first_name value"""
        self.assertEqual(hasattr(User, "first_name"), True)
        self.assertIs(type(User.first_name), str)
        self.assertEqual(User.first_name, "")

    def test_last_name_exists(self):
        """Tests the default last_name value"""
        self.assertEqual(hasattr(User, "last_name"), True)
        self.assertIs(type(User.last_name), str)
        self.assertEqual(User.last_name, "")
