#!/usr/bin/python3

"""This is the city class"""
from sqlalchemy import String, DateTime, Column, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base

class City(BaseModel, Base):
    """This is the class for City
    Attributes:
        state_id: The state id
        name: the name
    """
    __tablename__ = 'cities'
    
    # Renamed variables
    city_name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    places_relationship = relationship('Place', backref='city',
                                       cascade='all, delete-orphan')
