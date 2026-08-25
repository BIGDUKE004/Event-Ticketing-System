from datetime import date, time, datetime, timezone
from typing import Optional
from uuid import UUID, uuid4

from pydantic import BaseModel, Field

class Event(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    name: str
    description: str
    location: str
    date: date
    time: time
    organizer_id: UUID
    sold_out: bool = False
    created_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc)
    )
    updated_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc)
    )


    class CreateEvent(BaseModel):
        name: str
        description: str
        location: str
        organizer_id: str

    class UpdateEvent(BaseModel):
        name: Optional[str] = None
        description: Optional[str] = None
        location: Optional[str] = None
        organizer_id: Optional[str] = None

