#!/usr/bin/python3
"""This is the State class."""
from os import getenv
from sqlalchemy import String, DateTime, Column, ForeignKey
from sqlalchemy.orm import relationship
import models
from models.base_model import BaseModel, Base
from models.city import City

class State(BaseModel, Base):
    """This class represents the State model.
    
    Attributes:
        name (str): The name of the state.
    """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship('City', backref='state',
                              cascade='all, delete-orphan')
    else:
        @property
        def cities(self):
            """Getter attribute in case of file storage."""
            return [city for city in models.storage.all(City).values()
                    if city.state_id == self.id]
