#!/usr/bin/env python3

import models
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, create_engine
from models.base_model import Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from sqlalchemy.orm import sessionmaker, scoped_session
import os

class Db_storage():
    """
        New engine for datebase storage
    """
    __engine = None
    __session = None
    
    """
        Create connections
    """
    def __init__(self):
        """_summary_
        """
        
        user = os.getenv('HBNB_MYSQL_USER')
        passwd = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        db = os.getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine(f'mysql+mysqldb://{user}:{passwd}@127.0.0.1/{db}',
                                      pool_pre_ping=True)
        
        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)
            
    def all(self, cls=None):
        """ Returns in dictionary form the class

        Args:
            cls (_type_, optional): the class name to query
            Defaults to None.

        Returns:
            if class not none, return all object of the class
            else return all classes objects
        """
        objects = {}
        if cls:
            query_result = self.__session.query(cls).all()
        else:
            query_result = self.__session.query(User,
                                                State,
                                                City,
                                                Amenity,
                                                Review,
                                                Place),all()
        for cls_ in query_result:
            cls_key = cls.__class__.__name__ + '.' + cls.id
            objects[cls_key] = cls
        return objects
    
    def new(self, obj):
        """
            Add object to the current database
        Args:
            obj (_type_): the new object to add
        """
        self.__session.add(obj)
        
    def save(self):
        """
            Save all changes of the current database
        """    
        self.__session.commit()
        
    def delete(self, obj=None):
        """Delete from database obj if not none

        Args:
            obj (_type_, optional): object to delete. Defaults to None.
        """
        
        if obj is not None:
            self.__session.delete(obj)
        else:
            pass
    
    def reload(self):
        """
            create all tables in the database
        """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        
        self.__session = Session
        
    def close(self):
        """Close the working SQLAlchemy session."""
        self.__session.close()