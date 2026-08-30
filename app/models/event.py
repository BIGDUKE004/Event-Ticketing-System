from datetime import datetime, timezone
from typing import Optional
from uuid import UUID, uuid4

from pydantic import BaseModel, ConfigDict


class CreateEvent(BaseModel):
    name: str
    description: str
    location: str
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