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
        objAux = str(obj.__class__)
        idAux = str(obj.id)
        key = objAux + "." + idAux
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        dic_lis = {}
        for key in self.__objects:
            dic_lis[key] = self.__objects[key].to_dict()
        with open(self.__file_path, 'w', encoding="utf-8") as f:
            json.dump(dic_lis, f)

    def reload(self):
        """deserializes JSON file to __objects"""
        try:
            with open(self.__file_path, "r", encoding="utf=8") as f:
                x = json.load(f)
            for key, value in x.items():
                self.__objects[key] = BaseModel(**value)
        except FileNotFoundError:
            pass
