# SQL-Alchemy Imports
from sqlalchemy import Column, ForeignKey, Integer

# Local Backend Import
from .base import Base


class EventObjectRelationshipEntity(Base):
    __tablename__ = "event_object_relationship"

    event_object_relationship_id = Column(Integer, primary_key=True)
    event_id = Column(ForeignKey("event.event_id"), nullable=False)
    object_id = Column(ForeignKey("object.object_id"), nullable=False)
    qualifer_id = Column(ForeignKey("qualifer.qualifer_id"), nullable=False)
