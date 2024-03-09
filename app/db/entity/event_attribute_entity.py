# SQL-Alchemy Imports
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import mapped_column, Mapped, relationship

# Local Backend Import
from .base import Base


class EventAttributeEntity(Base):
    __tablename__ = "event_attribute"

    event_attribute_id = Column(Integer, primary_key=True)
    event_type_id: Mapped[int] = mapped_column(
        ForeignKey("event_type.event_type_id"), nullable=False
    )
    name = Column(String(255), default="")
    event_type: Mapped["EventTypeEntity"] = relationship(back_populates="event_attribute")
