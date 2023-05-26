from typing import List

from sqlalchemy.orm import Session

from models import User


class UsersRepository:

    def __init__(self, session: Session):
        self.__session = session

    def find_by_user_id(self, user_id: int) -> User:
        return self.__session.query(User).filter(User.user_id == user_id).first()

    def find_all_users(self) -> List[User]:
        return self.__session.query(User).all()

    def save_new_user(self, user: User):
        user_in_bd = self.find_by_user_id(user.user_id)
        if user_in_bd is None:
            self.__session.query(User).add_entity(user)
            self.__session.commit()
