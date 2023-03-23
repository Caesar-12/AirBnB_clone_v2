#!/usr/bin/python3

"""
Contains new engine DBStorage
"""

from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from models.base_model import Base
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine
import os


class DBStorage:
    """
    Storage system for Airbnb
    """

    __engine = None
    __session = None

    def __init__(self):
        user = os.getenv("HBNB_MYSQL_USER")
        pw = os.getenv("HBNB_MYSQL_PWD")
        host = os.getenv("HBNB_MYSQL_HOST")
        db = os.getenv("HBNB_MYSQL_DB")
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(user, pw, host, db),
                                      pool_pre_ping=True)
        self.__session = sessionmaker(bind=self.__engine)
        environ = os.getenv("HBNB_ENV")
        if environ == "test":
            Base.drop_all(self.__engine)

    def all(self, cls=None):
        new = {}
        if cls:
            for obj in self.__session.query(cls):
                key = "{}.{}".format(obj.__class__.__name__, obj.id)
                new[key] = obj
            return new
        else:
            classes = ("User", "State", "City", "Amenity", "Place", "Review")
            for clas in classes:
                for obj in self.__session.query(clas):
                    key = "{}.{}".format(obj.__class__.__name__, obj.id)
                    new[key] = obj
            return new

    def new(self, obj):
        """
        adds object to current database session
        """

        self.__session.add(obj)

    def save(self):
        """
        commit all changes of current database session
        """

        self.__session.commit()

    def delete(self, obj=None):
        """
        delete the current daabase session
        """

        if obj:
            self.__session.delete(obj)

    def reload(self):
        """
        creates all table in database
        """

        Base.metadata.create_all(self.__engine)
        sess = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess)
        self.__session = Session()
