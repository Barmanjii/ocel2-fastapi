# SQL-Alchemy Imports
from sqlalchemy import Column, Integer, String

# Local Backend Import
from .base import Base


class EventTypeEntity(Base):
    __tablename__ = "event_type"

    event_type_id = Column(Integer, primary_key=True)
    name = Column(String(255), default="")
