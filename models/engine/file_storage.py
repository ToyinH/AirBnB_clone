#!/usr/bin/python3
"""
Contains the FileStorage class
"""
from models.base_model import BaseModel
import json
from models.user import User


class FileStorage:
    """serializes instances to a JSON file & deserializes back to instances"""

    # string - path to the JSON file
    __file_path = "file.json"
    # dictionary - empty but will store all objects by <class name>.id
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
        json_objects = {}
        for key, value in self.__objects.items():
            json_objects[key] = value.to_dict()
        with open(self.__file_path, "w", encoding="utf") as file:
            json.dump(json_objects, file)

    def reload(self):
        try:
            with open(self.__file_path, 'r') as file:
                loaded_objects = json.load(file)
                for key, value in loaded_objects.items():
                    class_name, obj_id = key.split(".")
                    self.__objects[key] = eval(class_name)(**value)
        except FileNotFoundError:
            pass
