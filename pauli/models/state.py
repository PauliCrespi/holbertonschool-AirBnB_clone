#!/usr/bin/python3
"""State"""
from models.base_model import BaseModel


class State(BaseModel):
    """class state"""

    name = ""

    def __init__(self, *args, **kwargs):
        """class constructor"""
        super().__init__(*args, **kwargs)
