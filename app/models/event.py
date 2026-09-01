from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field

from app.models.ticket_type import TicketType


class CreateEvent(BaseModel):
    name: str = Field(min_length=1)
    description: str = Field(min_length=1)
    location: str = Field(min_length=1)
    organizer_id: str

class UpdateEvent(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    location: Optional[str] = None

class EventResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: UUID
    name: str
    description: str
    location: str
    organizer_id: str
    sold_out: bool
    created_at: datetime
    updated_at: datetime
    ticket_types: list[TicketType] = Field(default_factory=list)