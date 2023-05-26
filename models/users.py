from sqlalchemy import Column, Integer, String, Date

from utils import DbBase


class User(DbBase):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    first_name = Column(String)
    last_name = Column(String)
    username = Column(String)
    created_at = Column(Date)
