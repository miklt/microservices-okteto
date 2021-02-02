from sqlalchemy import Column, Integer, Float, String, Table, ForeignKey
from sqlalchemy.types import DateTime
from sqlalchemy.orm import relationship
import datetime

from .database import Base

class DictMixIn:
    def to_dict(self):
        return {
            column.name: getattr(self, column.name)
            if not isinstance(
                getattr(self, column.name), (datetime.datetime, datetime.date)
            )
            else getattr(self, column.name).isoformat()
            for column in self.__table__.columns
        }


class City(DictMixIn, Base):
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)   

class Temperature(DictMixIn, Base):
    __tablename__ = 'temperatures'
    id = Column(Integer, primary_key=True, autoincrement=True)
    city_id = Column(Integer, ForeignKey('cities.id'))
    value = Column(Float)
    date = Column(DateTime) 
    city = relationship("City")