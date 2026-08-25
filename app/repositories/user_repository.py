from abc import ABC, abstractmethod

from pydantic import BaseModel

from app.models import user


class UserRepository(ABC):

    @abstractmethod
    def save_user(self, user : user) -> user:
        pass

    @abstractmethod
    def update_user(self, user : user) -> user:
        pass

    @abstractmethod
    def delete_user(self, user_id : id) -> None:
        pass

    def get_user_by_id(self, user_id : id) -> user:
        pass

    def get_list_of_user(self):
        pass
