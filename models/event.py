from datetime import date, datetime
from typing import List, Optional
from pydantic import BaseModel, Field

from services import database


def generate_id():
    database.max_id += 1
    return database.max_id


class Event(BaseModel):
    id: int = Field(default_factory=generate_id, primary_key=True)
    create_time: datetime = Field(default_factory=datetime.now)
    name: str
    date: date
    time: str
    number_of_participants: int
    location: str
    description: Optional[str] = None
    tags: Optional[List[str]] = None
    forecast: str = None
