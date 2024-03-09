# SQL-Alchemy Imports
from sqlalchemy.sql import func
from sqlalchemy.dialects import postgresql as pg
from sqlalchemy import Column, ForeignKey, Integer, JSON

# Local Backend Import
from .base import Base


class ObjectAttributeValueEntity(Base):
    __tablename__ = "object_attribute_value"

    object_attribute_value_id = Column(Integer, primary_key=True)
    object_id = Column(ForeignKey("object.object_id"), nullable=False)
    object_attribute_id = Column(
        ForeignKey("object_attribute.object_attribute_id"), nullable=False
    )
    timestamp = Column(pg.TIMESTAMP(), nullable=False, default=func.now())
    value = Column(JSON, default={})
