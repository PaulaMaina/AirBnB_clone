#!/usr/bin/python3
"""Defines a TestCase for the file storage engine"""
import json
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import os
import unittest


class TestFileStorage(unittest.TestCase):
    """Defines the individual test cases for FileStorage"""
    def setUp(self):
        """Creates a FileStorage instance and sets file_path to test.json"""
        self.storage = FileStorage()
        FileStorage._FileStorage__file_path = "test.json"
        FileStorage._FileStorage__objects = {}
        self.storage.reload()

    def tearDown(self):
        """Deletes the test json file"""
        if os.path.exists("test.json"):
            os.remove("test.json")

    def test_file_path_exists(self):
        """Tests for the __file_path attribute value"""
        self.assertEqual(hasattr(FileStorage, "_FileStorage__file_path"), True)
        self.assertIs(type(FileStorage._FileStorage__file_path), str)

    def test_objects_exists(self):
        """Tests for the __objects attribute value"""
        self.assertEqual(hasattr(FileStorage, "_FileStorage__objects"), True)
        self.assertIs(type(FileStorage._FileStorage__objects), dict)
        self.assertEqual(FileStorage._FileStorage__objects, {})

    def test_all_default(self):
        """Tests all with default __objects attributes"""
        self.assertIs(type(self.storage.all()), dict)
        self.assertEqual(self.storage.all(), {})

    def test_all_BaseModel_instance(self):
        """Tests all command with one BaseModel instance"""
        instance = BaseModel()
        self.assertIs(type(self.storage.all()), dict)
        self.assertEqual(self.storage.all(), {
            "BaseModel." + instance.id: instance
        })

    def test_new(self):
        """Test new command with a BaseModel instance."""
        my_dict = {
            "__class__": "BaseModel",
            "id": "bbc29c6d-51a3-4b04-9dc3-ecccb3bc4cbe",
            "updated_at": "2024-03-10T21:01:23.479743",
            "created_at": "2024-03-10T21:01:23.479758"
        }
        key = "BaseModel.bbc29c6d-51a3-4b04-9dc3-ecccb3bc4cbe"
        instance = BaseModel(**my_dict)
        self.storage.new(instance)
        self.assertIn(key, self.storage.all())
        self.assertIs(self.storage.all()[key], instance)

    def test_save(self):
        """Test save command with a BaseModel instance"""
        my_dict = {
            "__class__": "BaseModel",
            "id": "bbc29c6d-51a3-4b04-9dc3-ecccb3bc4cbe",
            "updated_at": "2024-03-10T21:01:23.479743",
            "created_at": "2024-03-10T21:01:23.479758"
        }
        key = "BaseModel.bbc29c6d-51a3-4b04-9dc3-ecccb3bc4cbe"
        expected = {key: my_dict}
        instance = BaseModel(**my_dict)
        self.storage.new(instance)
        self.storage.save()
        with open("test.json", "r") as f:
            json_dict = json.load(f)
            self.assertEqual(json_dict, expected)

    def test_reload(self):
        """Test reload command with a BaseModel instance"""
        my_dict = {
            "__class__": "BaseModel",
            "id": "bbc29c6d-51a3-4b04-9dc3-ecccb3bc4cbe",
            "updated_at": "2024-03-10T21:01:23.479743",
            "created_at": "2024-03-10T21:01:23.479758"
        }
        key = "BaseModel.bbc29c6d-51a3-4b04-9dc3-ecccb3bc4cbe"
        instance = BaseModel(**my_dict)
        self.storage.new(instance)
        self.storage.save()
        self.storage.reload()
        self.assertEqual(len(self.storage.all().keys()), 1)
        self.assertIn(key, self.storage.all())
        self.assertEqual(self.storage.all()[key].to_dict(), my_dict)


if __name__ == '__main__':
    unittest.main()
