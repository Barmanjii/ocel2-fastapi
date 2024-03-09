# SQL-Alchemy Imports
from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import mapped_column, Mapped, relationship

# Local Backend Import
from .base import Base


class EventObjectRelationshipEntity(Base):
    __tablename__ = "event_object_relationship"

    event_object_relationship_id = Column(Integer, primary_key=True)
    event_id: Mapped[int] = mapped_column(ForeignKey("event.event_id"), nullable=False)
    object_id: Mapped[int] = mapped_column(
        ForeignKey("object.object_id"), nullable=False
    )
    qualifier_id: Mapped[int] = mapped_column(
        ForeignKey("qualifier.qualifier_id"), nullable=False
    )
    qualifier = relationship("QualifierEntity")
