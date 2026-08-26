from app.models.user import User
from app.repositories.user_repository import UserRepository


class InMemoryUserRepository(UserRepository):
    def __init__(self):
        self.users = []

    def save_user(self, user : User) -> User:
        self.users.append(user)
        return user

    def update_user(self, user : User) -> User:
        for people in self.users:
            if people.id == user.id:
                self.users.append(user)
        return user

    def get_user_by_id(self, user_id : id) -> User:
        for user in self.users:
            if user.id == user_id:
                return user

    def delete_user(self, user_id : id) -> None:
        self.users.remove(user_id)

    def get_list_of_user(self):
        return len(self.users)

    def get_user_by_email(self, email: str) -> User:
        for user in self.users:
            if user.email == email:
                return user
        return None