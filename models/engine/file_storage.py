#!/usr/bin/python3

import json
import os


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
            FileStorage.__objects = json.load(FileStorage.__file_path)
        else:
            pass
