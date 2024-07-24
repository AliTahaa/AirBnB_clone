#!/usr/bin/python3

import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review

class FileStorage():
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        FileStorage.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        objects = FileStorage.__objects
        obj_dict = {}
        for obj in objects.keys():
            obj_dict[obj] = objects[obj].to_dict()
        with open(FileStorage.__file_path, "w") as file:
            json.dump(obj_dict, file)

    def reload(self):
        """ This method deserializes the JSON file to __objects """
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r") as file:
                try:
                    obj_dict = json.load(file)

                    for key, value in obj_dict.items():
                        class_name, obj_id = key.split('.')

                        del value["__class__"]
                        cls = eval(class_name)

                        instance = cls(**value)

                        FileStorage.__objects[key] = instance
                except Exception:
                    pass
