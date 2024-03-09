# Main Python Import
from typing import List

# SQL-Alchemy Imports
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import Mapped, relationship

# Local Backend Import
from .base import Base


class ObjectTypeEntity(Base):
    __tablename__ = "object_type"

    object_type_id = Column(Integer, primary_key=True)
    name = Column(String(255), default="")
    object: Mapped[List["ObjectEntity"]] = relationship(back_populates="object_type")
    object_attribute = relationship("ObjectAttributeEntity")
