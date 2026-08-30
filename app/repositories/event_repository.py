from abc import ABC, abstractmethod
from typing import Optional, List
from uuid import UUID

from app.database_models.event import Event


class EventRepository(ABC):

    @abstractmethod
    def add(self, event: Event) -> Event:
        pass

    @abstractmethod
    def get(self, event_id: UUID) -> Optional[Event]:
        pass

    @abstractmethod
    def update(self, event_id: UUID, data: dict) -> Optional[Event]:
        pass

    @abstractmethod
    def get_all(self) -> List[Event]:
        pass

    @abstractmethod
    def delete(self, event_id: UUID) -> bool:
        pass