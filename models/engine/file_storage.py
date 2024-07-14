#!/usr/bin/python3
"""Defines the FileStorage class."""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
import os

class FileStorage:
    """Represent storage engine.

    Attributes:
        __file_path (str): string - path to the JSON file.
        __objects (dict): dictionary - empty but will store all objects.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        object_class_name = obj.__class__.__name__
        i = "{}.{}".format(object_class_name, obj.id)
        FileStorage.__objects[i] = obj

    def save(self):
        """serializes __objects to the JSON file."""
        objects = FileStorage.__objects
        obj_dict = {}
        for obj in objects.keys():
            obj_dict[obj] = objects[obj].to_dict()
        with open(FileStorage.__file_path, "w") as file:
            json.dump(obj_dict, file)

    def reload(self):
        """deserializes the JSON file to __objects."""

        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
                try:
                    obj_dict = json. load(file)
                    for key, value in obj_dict.items():
                        class_name, obj_id = key.split('.')

                        cls = eval(class_name)

                        instance = cls(**value)

                        FileStorage.__objects[key] = instance
                except Exception:
                    pass
