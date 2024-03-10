#!/usr/bin/python3
"""Child class of the BaseModel class"""
from models.base_model import BaseModel


class City(BaseModel):
    """Definition of the City class"""
    state_id = ""
    name = ""
