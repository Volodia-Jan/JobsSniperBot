from sqlalchemy import Column, Integer, ForeignKey, String, Date

from utils import DbBase


class Job(DbBase):
    __tablename__ = 'jobs'
    job_id = Column(Integer, primary_key=True)
    job_name = Column(String)
    job_description = Column(String)
    salary = Column(Integer, default=0)
    city_id = Column(Integer, ForeignKey('cities.city_id'))
    employment_type_id = Column(Integer, ForeignKey('employment_types.emp_type_id'))
    work_place_id = Column(Integer, ForeignKey('work_places.work_place_id'))
    experience = Column(Integer, default=0)
    created_at = Column(Date)
