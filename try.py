#!/usr/bin/python3
"""BaseModel class"""

from uuid import uuid4
from datetime import datetime


class BaseModel():
    """BaseModel class"""
    def __init__(self, *args, **kwargs):
        print(self.__dict__)
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs != None:
            for key, value in kwargs.items():
                self.__dict__[key] = value
            

    def __str__(self):
        class_name = self.__class__.__name__
        id = self.id
        data = self.__dict__
        return"[{}] ({}) {}".format(class_name, id, data)

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        data = self.__dict__.copy()
        data["__class__"] = self.__class__.__name__
        data["created_at"] = datetime.now().isoformat()
        data["updated_at"] = datetime.now().isoformat()
        return data

my_model = BaseModel()
