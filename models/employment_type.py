from sqlalchemy import Column, Integer, String

from utils import DbBase


class EmploymentType(DbBase):
    __tablename__ = 'employment_types'
    emp_type_id = Column(Integer, primary_key=True)
    type_name = Column(String)
