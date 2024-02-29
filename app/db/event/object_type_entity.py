# SQL-Alchemy Imports
from sqlalchemy import Column, String, Integer

# Local Backend Import
from .base import Base


class ObjectTypeEntity(Base):
    __tablename__ = "object_type"

    object_type_id = Column(Integer, primary_key=True)
    name = Column(String(255), default="")
