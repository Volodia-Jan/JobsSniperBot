from typing import List

from sqlalchemy.orm import Session

from models import WorkPlace


class WorkPlacesRepository:

    def __init__(self, session: Session):
        self.__session = session

    def find_all_work_places(self) -> List[WorkPlace]:
        return self.__session.query(WorkPlace).all()

    def find_work_place_by_id(self, work_place_id: int) -> WorkPlace:
        return self.__session.query(WorkPlace).filter(WorkPlace.work_place_id == work_place_id).first()
