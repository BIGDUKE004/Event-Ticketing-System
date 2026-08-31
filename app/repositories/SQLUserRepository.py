from sqlalchemy import text, select
from sqlalchemy.orm import Session

from app.database_models.user import User
from app.repositories.user_repository import UserRepository


class SQLUserRepository(UserRepository):
    def __init__(self, db: Session):
        self.db = db

    def save_user(self, user : User) -> User:
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def update_user(self, user: User) -> User:
        self.db.commit()
        self.db.refresh(user)
        return user

    def get_user_by_id(self, user_id : id) -> User:
        user = self.get_user_by_id(user_id)
        if user is None:
            return None
        return user


    def delete_user(self, user_id : id) -> None:
        user = self.get_user_by_id(user_id)
        if user is None:
            return None
        self.db.delete(user)
        self.db.commit()
        self.db.refresh(user)


    def get_list_of_user(self):
        return self.db.query(User).all()

    def get_user_by_email(self, email: str):
        result = self.db.execute(
            select(User).where(User.email == email)
        )

        return result.scalar_one_or_none()
