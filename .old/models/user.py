#!/usr/bin/python3
"""the User class."""
from models.base_model import BaseModel


class User(BaseModel):
    """Represent a User.

    Attributes:
        email: string - empty string.
        password: string - empty string.
        first_name: string - empty string.
        last_name: string - empty string.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
