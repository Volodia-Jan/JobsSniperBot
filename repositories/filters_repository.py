from typing import List

from sqlalchemy.orm import Session

from models import Filter


class FiltersRepository:

    def __init__(self, session: Session):
        self.__session = session

    def find_all_filters_by_user_id(self, user_id: int) -> List[Filter]:
        return self.__session.query(Filter).filter(Filter.user_id == user_id).all()

    def find_filter_by_name(self, filter_name: str, user_id: int):
        return self.__session.query(Filter).filter(
            Filter.user_id == user_id and Filter.filter_name == filter_name).first()

    def add_new_filter(self, user_filter: Filter):
        filer = self.find_filter_by_name(user_filter.filter_name, user_filter.user_id)
        if filer is None:
            self.__session.query(Filter).add_entity(user_filter)
            self.__session.commit()
