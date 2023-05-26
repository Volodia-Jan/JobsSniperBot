from sqlalchemy import Column, Integer, ForeignKey, String

from utils import DbBase


class Filter(DbBase):
    __tablename__ = 'filters'
    filter_id = Column(Integer, primary_key=True)
    filter_name = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
    city_id = Column(Integer, ForeignKey('cities.city_id'))
    employment_type_id = Column(Integer, ForeignKey('employment_types.emp_type_id'))
    work_place_id = Column(Integer, ForeignKey('work_places.work_place_id'))
    experience = Column(Integer, default=0)
