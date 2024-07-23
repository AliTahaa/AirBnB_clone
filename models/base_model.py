#!/usr/bin/python3
"""BaseModel class"""

from uuid import uuid4
from datetime import datetime
import models


class BaseModel():
    """BaseModel class"""
    def __init__(self, *args, **kwargs):
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs is not None:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value, t_format)
                else:
                    self.__dict__[key] = value
        models.storage.new(self)

    def __str__(self):
        class_name = self.__class__.__name__
        id = self.id
        data = self.__dict__
        return "[{}] ({}) {}".format(class_name, id, data)

    def save(self):
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        data = self.__dict__.copy()
        data["__class__"] = self.__class__.__name__
        data["created_at"] = datetime.now().isoformat()
        data["updated_at"] = datetime.now().isoformat()
        return data
