import uuid
from typing import Optional
from pydantic import BaseModel, Field



class CreateTicketType(BaseModel):
    event_id: str
    name: str
    price: float = Field(gt=0)
    quantity: int = Field(gt=0)

class UpdateTicketType(BaseModel):
    event_id: Optional[str] = None
    name: Optional[str] = None
    price: Optional[float] = None
    quantity: Optional[int] = None

class TicketType(BaseModel):
    id : uuid.UUID = Field(default_factory=uuid.uuid4)
    event_id : str
    name : str
    price : float
    quantity : int
    available_quantity : int
    sold_out: bool
