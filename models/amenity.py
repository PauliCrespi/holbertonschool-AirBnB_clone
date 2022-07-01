#!/usr/bin/python3
"""amenity"""


from models.base_model import BaseModel


class Amenity(BaseModel):
    """class amenity"""

    name = ""

    def __init__(self, *args, **kwargs):
        """class constructor"""
        super().__init__(*args, **kwargs)
