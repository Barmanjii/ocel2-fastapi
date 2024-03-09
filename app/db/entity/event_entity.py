# SQL-Alchemy Imports
from sqlalchemy.sql import func
from sqlalchemy.dialects import postgresql as pg
from sqlalchemy import Column, ForeignKey, Integer

# Local Backend Import
from .base import Base


class EventEntity(Base):
    __tablename__ = "event"

    event_id = Column(Integer, primary_key=True)
    event_type_id = Column(ForeignKey("event_type.event_type_id"), nullable=False)
    timestamp = Column(pg.TIMESTAMP(), nullable=False, default=func.now())
