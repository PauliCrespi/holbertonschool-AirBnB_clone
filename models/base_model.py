#!/usr/bin/python3
"""base model"""
import uuid
import datetime

class BaseModel:
    """class model"""

    def __init__(self):
        """init"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now().isoformat()
        self.updated_at = datetime.datetime.now().isoformat()

    def __str__(self):
        """str representation"""
        return("[BaseModel] ({}) {}".format(self.id, self.__dict__))

    def save(self):
        """saves"""
        setattr(self, self.updated_at, datetime.datetime.now().isoformat())

    def to_dict(self):
        """returns dictionary of the instance"""
    

