#!/usr/bin/python3
"""File Storage"""

from models.base_model import BaseModel
import json


model = {"BaseModel": BaseModel}


class FileStorage:
    """class FileStorage"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        if obj is not None:
            key = obj.__class__.__name__ + "." + obj.id
            self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        json_obj = {}
        for key in self.__objects:
            json_obj[key] = self.__objects[key].to_dict()
        with open(self.__file_path, "w", encoding="utf=8") as f:
            json.dump(json_obj, f)

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, "r", encoding="utf=8") as f:
                jsob = json.load(f)
            for key, value in jsob.items():
                self.__objects[key] = BaseModel(**value)
        except FileNotFoundError:
            pass

