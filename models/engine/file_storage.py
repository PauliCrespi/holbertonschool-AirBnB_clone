#!/usr/bin/python3
"""File Storage"""



class FileStorage:
    """class FileStorage"""
    def __init__(self, file_path, objects):
        """inisialization"""
        self.__file_path = file_path
        self.__objects = objects

    @property
    def all(self):
        """returns the dictionary __objects"""
        return self.__file_path

    @new.setter
    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
    self.__objects = obj.get('__class__') + "." + obj.get(id)

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        dic_lis = []
        if list_objs is None:
            list_objs = []
        for c in list_objs:
            dic_lis.append(c.to_dictionary())
        with open(self.__file_path, 'w', encoding="utf-8") as f:
            f.write(self.(self.__objects ))

