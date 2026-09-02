from abc import ABC, abstractmethod
from uuid import UUID

from pydantic import BaseModel

from app.models import user
from app.database_models.user import User

class UserRepository(ABC):

    @abstractmethod
    def save_user(self, user : User) -> User:
        pass

    @abstractmethod
    def update_user(self, user : User) -> User:
        pass

    @abstractmethod
    def delete_user(self, user_id : UUID) -> None:
        pass

    def get_user_by_id(self, user_id : UUID) -> User:
        pass

    def get_user_by_email(self, email: str) -> User:
        pass

    def get_list_of_user(self):
        pass
