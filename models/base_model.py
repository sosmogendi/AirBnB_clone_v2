#!/usr/bin/python3
"""This is the BaseModel class for the AirBnB project."""
import uuid
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import String, DateTime, Column
import models

Base = declarative_base()

class BaseModel:
    """This class defines all common attributes and methods for other classes."""

    id = Column(String(60), unique=True, nullable=False, primary_key=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Instantiation of the BaseModel class."""
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
            if "id" not in kwargs.keys():
                setattr(self, "id", str(uuid.uuid4()))
            time = datetime.now()
            if "created_at" not in kwargs.keys():
                setattr(self, "created_at", time)
            if "updated_at" not in kwargs.keys():
                setattr(self, "updated_at", time)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()

    def __str__(self):
        """Returns a string representation of the object."""
        dic = self.to_dict()
        return "[{}] ({}) {}".format(
            type(self).__name__, self.id, dic)

    def __repr__(self):
        """Returns a string representation of the object."""
        return self.__str__()

    def save(self):
        """Updates the public instance attribute updated_at to the current time."""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Creates a dictionary representation of the object."""
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = type(self).__name__
        my_dict["created_at"] = my_dict["created_at"].isoformat()
        my_dict["updated_at"] = my_dict["updated_at"].isoformat()
        if '_sa_instance_state' in my_dict.keys():
            my_dict.pop('_sa_instance_state', None)
        return my_dict

    def delete(self):
        """Deletes the current instance from the storage (models.storage)."""
        models.storage.delete(self)
