# Main Python Import
from typing import List

# SQL-Alchemy Imports
from sqlalchemy import Column, JSON, Integer
from sqlalchemy.orm import Mapped, relationship

# Local Backend Import
from .base import Base


class QualifierEntity(Base):
    __tablename__ = "qualifier"

    qualifier_id = Column(Integer, primary_key=True)
    value = Column(JSON, default={})
    event_object: Mapped[List["EventObjectRelationshipEntity"]] = relationship(
        back_populates="qualifier"
    )
    object: Mapped[List["ObjectRelationshipEntity"]] = relationship(
        back_populates="qualifier"
    )
