from sqlalchemy import Column, Integer, String

from utils import DbBase


class WorkPlace(DbBase):
    __tablename__ = 'work_places'
    work_place_id = Column(Integer, primary_key=True)
    work_place_name = Column(String)
