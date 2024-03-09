# Main Python Import
from typing import List

# SQL-Alchemy Imports
from sqlalchemy.sql import func
from sqlalchemy.dialects import postgresql as pg
from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import Mapped, relationship, mapped_column

# Local Backend Import
from .base import Base


class EventEntity(Base):
    __tablename__ = "event"

    event_id = Column(Integer, primary_key=True)
    event_type_id: Mapped[int] = mapped_column(
        ForeignKey("event_type.event_type_id"), nullable=False
    )
    timestamp = Column(pg.TIMESTAMP(), nullable=False, default=func.now())

    event_type: Mapped["EventTypeEntity"] = relationship(back_populates="event")
    event_attribute_value = relationship("EventAttributeValueEntity")
