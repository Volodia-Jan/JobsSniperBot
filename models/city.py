from sqlalchemy import Column, Integer, String
from utils import DbBase


class City(DbBase):
    __tablename__ = 'cities'
    city_id = Column(Integer, primary_key=True)
    city_name = Column(String)
