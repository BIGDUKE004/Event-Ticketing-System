import uuid

from pydantic import BaseModel, Field


class TicketType(BaseModel):
    id : uuid.UUID = Field(default_factory=uuid.uuid4)
    event_id : str
    name : str
    price : float
    quantity : int
    available_quantity : int
    sold_out: bool