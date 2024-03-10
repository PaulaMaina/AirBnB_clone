#!/usr/bin/python3
"""Child class of BaseModel"""
from models.base_model import BaseModel


class User(BaseModel):
    """Definition of the User class"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
