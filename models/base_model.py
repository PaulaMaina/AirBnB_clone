#!/usr/bin/python3
"""Defines all common attributes and methods for other classes"""
from datetime import datetime
import models
import uuid


class BaseModel:
    """Definition of the BaseModel class"""
    def __init__(self, *args, **kwargs):
        """Initializes an instance of the BaseModel class"""
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.strptime(value,
                            "%Y-%m-%dT%H:%M:%S.%f"))
                elif key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """Displays the string format of an instance"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     self.__dict__)

    def save(self):
        """Updates the updated_at attribute with the current date and time"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of the instance"""
        dict_new = self.__dict__.copy()
        dict_new["__class__"] = self.__class__.__name__
        dict_new["created_at"] = self.created_at.isoformat()
        dict_new["updated_at"] = self.updated_at.isoformat()
        return dict_new
