#!/usr/bin/python3
"""Defines the Amenity class."""
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy import String
from sqlalchemy.orm import relationship
from os import getenv


class Amenity(BaseModel, Base):
    """Represents an Amenity for a MySQL database.

    Inherits from SQLAlchemy Base and links to the MySQL table amenities.

    Attributes:
        __tablename__ (str): The name of the MySQL table to store Amenities.
        name (sqlalchemy String): The amenity name.
        place_amenities (sqlalchemy relationship): Place-Amenity relationship.
    """
    if getenv("HBNB_TYPE_STORAGE") != "db":
        __tablename__ = "amenities"
        name = Column(String(128), nullable=False)
    else:
        name = ""
    
    def __init__(self, *args, **kwargs):
        """Initializes Amenity"""
        super().__init__(*args, **kwargs)