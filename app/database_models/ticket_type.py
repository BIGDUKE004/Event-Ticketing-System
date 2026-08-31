import uuid

from sqlalchemy import Boolean, Float, Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class TicketTypeDB(Base):
    __tablename__ = "ticket_types"

    id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
        default=lambda: str(uuid.uuid4()),
        nullable=False
    )

    event_id: Mapped[str] = mapped_column(
        String(36),
        ForeignKey("event.id"),
        nullable=False
    )

    name: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    price: Mapped[float] = mapped_column(
        Float,
        nullable=False
    )

    quantity: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )

    available_quantity: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )

    sold_out: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=False
    )