# SQL-Alchemy Imports
from sqlalchemy import Column, ForeignKey, Integer

# Local Backend Import
from .base import Base


class ObjectEntity(Base):
    __tablename__ = "object"

    object_id = Column(Integer, primary_key=True)
    object_type_id = Column(ForeignKey("object_type.object_type_id"), nullable=False)
