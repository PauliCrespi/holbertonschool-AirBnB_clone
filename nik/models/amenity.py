#!/usr/bin/python3
"""amenity"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """amenity class"""

    name = ""

    def __init__(self, *args, **kwargs):
        """class init"""
        super().__init__(*args, **kwargs)
