#!/usr/bin/python3
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
import models
from models.city import City


class State(BaseModel, Base):
    """This is the class for State.

    Attributes:
        name (str): The name of the state.
    """

    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    # For DBStorage
    cities = relationship("City", cascade='all, delete', backref="state")

    # For FileStorage, the getter attribute cities can remain as-is
    @property
    def cities(self):
        """Getter attribute to retrieve a list of City instances associated with this state.

        Returns:
            list: A list of City instances.
        """
        var = models.storage.all()
        lista = []
        result = []
        for key in var:
            city = key.replace('.', ' ')
            city = shlex.split(city)
            if (city[0] == 'City'):
                lista.append(var[key])
        for elem in lista:
            if (elem.state_id == self.id):
                result.append(elem)
        return (result)
