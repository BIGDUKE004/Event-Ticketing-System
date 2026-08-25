import uuid
from dataclasses import field

from pydantic import BaseModel


class TicketType(BaseModel):
    id : uuid.UUID = field(default=uuid.uuid4)
    event_id : str
    name : str
    price : float
    quantity : int
    available_quantity : int
    sold_out: bool