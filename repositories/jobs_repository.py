from typing import List
from models import Job

from sqlalchemy.orm import Session


class JobsRepository:

    def __init__(self, session: Session):
        self.__session = session

    def find_all_jobs(self) -> List[Job]:
        return self.__session.query(Job).all()

    def find_job_by_id(self, job_id: int):
        return self.__session.query(Job).filter(Job.job_id == job_id).first()
