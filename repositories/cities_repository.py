from typing import List

from sqlalchemy.orm import Session

from models import City


class CitiesRepository:

    def __init__(self, session: Session):
        self.__session = session

    def find_all_cities(self) -> List[City]:
        return self.__session.query(City).all()

    def find_cities_by_id(self, city_id: int):
        return self.__session.query(City).filter(City.city_id == city_id).first()
