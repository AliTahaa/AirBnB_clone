#!/usr/bin/python3

import json
import os
from models.base_model import BaseModel

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
        """deserializes the JSON file to __objects."""
        try:
            with open(FileStorage.__file_path) as file:
                obj_dict = json.load(file)
                for i in obj_dict.values():
                    class_name = i["__class__"]
                    del i["__class__"]
                    self.new(eval(class_name)(**i))
        except FileNotFoundError:
            return
