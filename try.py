#!/usr/bin/python3

from uuid import uuid4
from datetime import datetime

id = uuid4()

created_at = datetime.now()

class info():
  def __init__(self):
    self.id = uuid4()

do = info()

print(do.id)
