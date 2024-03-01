# SQL-Alchemy Imports
from sqlalchemy import Column, ForeignKey, Integer, String

# Local Backend Import
from .base import Base


class ObjectAttributeEntity(Base):
    __tablename__ = "object_attribute"

    object_attribute_id = Column(Integer, primary_key=True)
    object_type_id = Column(ForeignKey("object_type.object_type_id"), nullable=False)
    name = Column(String(255), default="")
