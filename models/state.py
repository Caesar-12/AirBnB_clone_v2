#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
import os
from models.city import City
import models


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    # st = os.getenv("HBNB_TYPE_STORAGE")
    cities = relationship("City", cascade='all, delete, delete-orphan',
                          backref="state")

    @property
    def cities(self):
        city_list = []
        stateCity = []
        allObj = models.storage.all()
        for k, v in allObj.items():
            cls = k.split(".")
            if cls[0] == 'City':
                city_list.append(allObj[k])
        for city in city_list:
            if city.state_id == self.id:
                stateCity.append(city)
        return stateCity
