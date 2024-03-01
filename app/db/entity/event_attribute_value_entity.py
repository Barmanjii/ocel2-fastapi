# SQL-Alchemy Imports
from sqlalchemy import Column, ForeignKey, Integer, JSON

# Local Backend Import
from .base import Base


class EventAttributeValueEntity(Base):
    __tablename__ = "event_attribute_value"

    event_attribute_value_id = Column(Integer, primary_key=True)
    event_id = Column(ForeignKey("event.event_id"), nullable=False)
    event_attribute_id = Column(
        ForeignKey("event_attribute.event_attribute_id"), nullable=False
    )
    value = Column(JSON, default={})
