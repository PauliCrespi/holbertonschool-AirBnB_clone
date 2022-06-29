#!/usr/bin/python3
"""users"""
from models.base_model import BaseModel


class User(BaseModel):
    """user class"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """init class"""
        super().init(*args, **kwargs)
