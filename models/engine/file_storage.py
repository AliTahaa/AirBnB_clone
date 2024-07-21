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
        with open(FileStorage.__file_path, "w") as file:
            json.dump(FileStorage.__objects, file)

    def reload(self):
        if os.path.exists(FileStorage.__file_path):
            with open(self.__file_path, 'r') as f:
                objs = json.load(f)
                for key, value in objs.items():
                    class_name = value["__class__"]
                    del value["__class__"]
                    if class_name == 'BaseModel':
                        self.__objects[key] = BaseModel(**value)
        else:
            pass
