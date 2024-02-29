# SQL-Alchemy Imports
from sqlalchemy import Column, ForeignKey, Integer, String

# Local Backend Import
from .base import Base


class EventAttributeEntity(Base):
    __tablename__ = "event_attribute"

    event_attribute_id = Column(Integer, primary_key=True)
    event_type_id = Column(ForeignKey("event_type.event_type_id"), nullable=False)
    name = Column(String(255), default="")
