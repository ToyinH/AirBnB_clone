#!/usr/bin/python3
"""
a class BaseModel that defines
all common attributes/methods for other classes
"""
from datetime import datetime
import uuid


class BaseModel:
    """
    The BaseModel class that defines all common methods
    and attributes for other classes.
    """
    def __init__(self):
        """
        class constructor for BaseModel
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """
        the __str__ method
        """
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        method that updates the public attribut update_at"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        """
        obj_dict = self.__dict__.copy()
        obj_dict["__class__"] = self.__class__.__name__
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()
        return obj_dict
