#!/usr/bin/python3
"""TestCases for the BaseModel class"""
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import os
import unittest


class TestBaseModel(unittest.TestCase):
    """Defines the individual tests for BaseModel class"""
    def setUp(self):
        """Creates a FileStorage instance and sets file_path to test.json"""
        self.storage = FileStorage()
        FileStorage._FileStorage__file_path = "test.json"
        self.storage.reload()

    def tearDown(self):
        """Deletes the test json file"""
        if os.path.exists("test.json"):
            os.remove("test.json")

    def test_id_string_type(self):
        """Tests if the ID is a str"""
        self.assertEqual(type(BaseModel().id), str)

    def test_id_unique(self):
        """Tests if the ID vakues are unique"""
        unique_ids = set()
        for i in range(1000):
            instance = BaseModel()
            self.assertNotIn(instance.id, unique_ids)
            unique_ids.add(instance.id)

    def test_created_at_type(self):
        """Tests if created_at is a datetime"""
        instance = BaseModel()
        self.assertEqual(type(instance.created_at), datetime)

    def test_updated_at_type(self):
        """Tests if updated_at is a datetime"""
        instance = BaseModel()
        self.assertEqual(type(instance.updated_at), datetime)

    def test_str(self):
        """Tests if __str__ returns [<cls name>] (<id>) <__dict__>"""
        instance = BaseModel()
        expected = "[{}] ({}) {}".format(instance.__class__.__name__,
                                         instance.id, instance.__dict__)
        self.assertEqual(str(instance), expected)

    def test_save_updated(self):
        """Tests if save function changes updated_at"""
        instance = BaseModel()
        old_datetime = instance.updated_at
        instance.save()
        self.assertLess(old_datetime, instance.updated_at)

    def test_to_dict_type(self):
        """Tests if to_dict function returns a dictionary"""
        instance = BaseModel()
        self.assertEqual(type(instance.to_dict()), dict)

    def test_to_dict_values(self):
        """Tests if to_dict function has the correct key-value pairs"""
        instance = BaseModel()

        new_dict = instance.__dict__.copy()
        new_dict["__class__"] = instance.__class__.__name__
        new_dict["created_at"] = instance.created_at.isoformat()
        new_dict["updated_at"] = instance.updated_at.isoformat()

        self.assertIn("__class__", instance.to_dict())
        self.assertIn("id", instance.to_dict())
        self.assertIn("created_at", instance.to_dict())
        self.assertIn("updated_at", instance.to_dict())
        self.assertEqual(new_dict, instance.to_dict())

    def test_to_dict_new_attrs(self):
        """Tests if to_dict function contains added attributes"""
        instance = BaseModel()
        instance.name = "ALX"
        instance.my_number = 89

        new_dict = instance.__dict__.copy()
        new_dict["__class__"] = instance.__class__.__name__
        new_dict["created_at"] = instance.created_at.isoformat()
        new_dict["updated_at"] = instance.updated_at.isoformat()

        self.assertIn("name", instance.to_dict())
        self.assertIn("my_number", instance.to_dict())
        self.assertEqual(new_dict, instance.to_dict())


if __name__ == '__main__':
    unittest.main()
