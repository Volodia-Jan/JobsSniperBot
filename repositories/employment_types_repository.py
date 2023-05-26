from typing import List

from sqlalchemy.orm import Session

from models import EmploymentType


class EmploymentTypesRepository:

    def __init__(self, session: Session):
        self.__session = session

    def find_all_employment_types(self) -> List[EmploymentType]:
        return self.__session.query(EmploymentType).all()

    def find_employment_type_by_id(self, employment_type_id: int) -> EmploymentType:
        return self.__session.query(EmploymentType).filter(EmploymentType.emp_type_id == employment_type_id).first()
