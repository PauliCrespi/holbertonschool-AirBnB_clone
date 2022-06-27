#!/usr/bin/python3
"""base model"""
import uuid
import datetime

class BaseModel:
    """class model"""

    def __init__(self):
        """init"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        """str representation"""
        return("[BaseModel] ({}) {}".format(self.id, self.__dict__))

    def save(self):
        """saves"""
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """returns dictionary of the instance"""
        self.created_at = self.created_at.isoformat()
        self.updated_at = self.updated_at.isoformat()
        dAux = self.__dict__
        dAux["__class__"] = "BaseModel"
        return dAux

