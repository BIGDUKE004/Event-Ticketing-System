import uuid

from sqlalchemy import String, Boolean
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base
from app.models import users_enum

class User(Base):
    __tablename__ = "user"
    id: Mapped[uuid.UUID] = mapped_column(
        String(36),
        primary_key=True,
        default=uuid.uuid4,
        nullable=False,
    )

    name: Mapped[str] = mapped_column(
        String(36),
        nullable=False,
    )

    email: Mapped[str] = mapped_column(
        String(36),
        nullable=False,
    )

    password: Mapped[str] = mapped_column(
        String(36),
        nullable=False,
    )

    role: Mapped[users_enum.UserRole] = mapped_column(
        String(36),
        nullable=False,
    )

    isLoggedIn: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=False,
    )