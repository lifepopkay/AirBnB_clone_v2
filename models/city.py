#!/usr/bin/python3
"""Defines the City class."""
from models.base_model import Base
from models.base_model import BaseModel
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import relationship
from os import getenv


class City(BaseModel, Base):
    """Represents a city for a MySQL database."""

    if getenv("HBNB_TYPE_STORAGE") != "db":
        __tablename__ = "cities"
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
        places = relationship("Place", backref="cities")
    else:
        state_id = ""
        name = ""
        
    def __init__(self, *args, **kwargs):
        """initializing city"""
        super().__init__(*args, **kwargs)
