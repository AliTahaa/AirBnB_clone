#!/usr/bin/python3
"""the BaseModel class."""
from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """Represents the BaseModel"""

    def __init__(self, *args, **kwargs):
        """Initialize new BaseModel.

        Args:
            *args (any):  wont be used.
            **kwargs (dict): each key of this dictionary is an attribute name.
        """
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value, time_format)
                else:
                    self.__dict__[key] = value
        else:
            models.storage.new(self)

    def save(self):
        """save current datetime."""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """Return the dictionary of the BaseModel."""
        instance_dict = self.__dict__.copy()
        instance_dict["__class__"] = self.__class__.__name__
        instance_dict["created_at"] = self.created_at.isoformat()
        instance_dict["updated_at"] = self.updated_at.isoformat()
        return instance_dict

    def __str__(self):
        """Return the representation of the BaseModel."""
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)
