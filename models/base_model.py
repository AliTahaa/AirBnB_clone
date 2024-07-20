#!/usr/bin/python3
'''Basemodel class'''

from uuid import uuid4
from datetime import datetime


class BaseModel():
    '''Basemodel class'''
    def __init__(self):
        self.id = str(uuid4())
        self.created_at = str(datetime.now().isoformat())
        self.updated_at = str(datetime.now().isoformat())

    def __str__(self):
        class_name = self.__class__.__name__
        id = self.id
        data = self.__dict__
        print("[{}] ({}) {}".format(class_name, id, data))

    def save(self):
        self.updated_at = str(datetime.now().isoformat())

    def to_dict(self):
        data = self.__dict__.copy()
        data["__class__"] = self.__class__.__name__
        data["created_at"] = str(datetime.now().isoformat())
        data["updated_at"] = str(datetime.now().isoformat())
        return data