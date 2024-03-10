#!/usr/bin/python3
"""The FileStorage class serializes instances to a JSON file and vice versa"""
import json
from models.base_model import BaseModel
from pathlib import Path


class FileStorage:
    """Definition of the FileStorage class"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the private objects dictionary"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets the obj with a key in __objects"""
        obj_key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[obj_key] = obj

    def save(self):
        """Serializes objects to the JSON file"""
        my_dict = {key: value.to_dict()
                   for key, value in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(my_dict, f)

    def reload(self):
        """Deserializes the JSON file to objects"""
        filepath = Path(FileStorage.__file_path)
        if filepath.is_file():
            with open(FileStorage.__file_path, "r") as f:
                FileStorage.__objects = {key: BaseModel(**value) for key, value
                                         in json.load(f).items()}
