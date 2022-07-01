#!/usr/bin/python3
"""review"""
from models.base_model import BaseModel


class Review(BaseModel):
    """class review"""

    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """class constructor"""
        super().__init__(*args, **kwargs)
