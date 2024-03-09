# Main Python Import
from typing import List

# SQL-Alchemy Imports
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Mapped, relationship

# Local Backend Import
from .base import Base


class EventTypeEntity(Base):
    __tablename__ = "event_type"

    event_type_id = Column(Integer, primary_key=True)
    name = Column(String(255), default="")

    event: Mapped[List["EventEntity"]] = relationship(back_populates="event_type")
    event_attribute = relationship("EventAttributeEntity")
