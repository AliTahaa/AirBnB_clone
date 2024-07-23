#!/usr/bin/python3
"""BaseModel class"""

from models.base_model import BaseModel
from models import storage


my_model = BaseModel()
my_model.save()
print(my_model)
