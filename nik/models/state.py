#!/usr/bin/python3
"""states"""
from models.base_model import BaseModel


class State(BaseModel):
    """state class"""

    name = ""

    def __init__(self, *args, **kwargs):
        """class init"""
        super().__init__(*args, **kwargs)
