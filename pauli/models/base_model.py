#!/usr/bin/python3
"""base model"""
import uuid
import datetime
import  models

class BaseModel:
    """class model"""

    def __init__(self, *args, **kwargs):
        """init"""
        if kwargs is not None and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key == "created_at":
                        value = datetime.datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                    elif key == "updated_at":
                        value = datetime.datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                    setattr(self, key, value)
        else:
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            self.id = str(uuid.uuid4())
            models.storage.new(self)

    def __str__(self):
        """str representation"""
        return("[BaseModel] ({}) {}".format(self.id, self.__dict__))

    def save(self):
        """saves"""
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns dictionary of the instance"""
        dAux = self.__dict__.copy()
        for key in dAux:
            if key == "created_at":
                dAux[key] = dAux[key].isoformat()
            elif key == "updated_at":
                dAux[key] = dAux[key].isoformat()
        dAux["__class__"] = "BaseModel"
        return dAux

