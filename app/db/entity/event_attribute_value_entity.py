# SQL-Alchemy Imports
from sqlalchemy import Column, ForeignKey, Integer, JSON
from sqlalchemy.orm import Mapped, mapped_column, relationship

# Local Backend Import
from .base import Base


class EventAttributeValueEntity(Base):
    __tablename__ = "event_attribute_value"

    event_attribute_value_id = Column(Integer, primary_key=True)
    event_id: Mapped[int] = mapped_column(ForeignKey("event.event_id"), nullable=False)
    event_attribute_id: Mapped[int] = mapped_column(
        ForeignKey("event_attribute.event_attribute_id"), nullable=False
    )
    value = Column(JSON, default={})

    event = relationship("EventEntity", back_populates="event_attribute_value")

    event_attribute = relationship(
        "EventAttributeEntity", back_populates="event_attribute_value"
    )
