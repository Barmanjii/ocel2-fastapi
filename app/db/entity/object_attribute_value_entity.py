# SQL-Alchemy Imports
from sqlalchemy.sql import func
from sqlalchemy.dialects import postgresql as pg
from sqlalchemy import Column, ForeignKey, Integer, JSON
from sqlalchemy.orm import Mapped, mapped_column, relationship

# Local Backend Import
from .base import Base


class ObjectAttributeValueEntity(Base):
    __tablename__ = "object_attribute_value"

    object_attribute_value_id = Column(Integer, primary_key=True)
    object_id: Mapped[int] = mapped_column(
        ForeignKey("object.object_id"), nullable=False
    )
    object_attribute_id: Mapped[int] = mapped_column(
        ForeignKey("object_attribute.object_attribute_id"), nullable=False
    )
    timestamp = Column(pg.TIMESTAMP(), nullable=False, default=func.now())
    value = Column(JSON, default={})

    object = relationship("ObjectEntity", back_populates="Object_attribute_value")

    object_attribute = relationship(
        "ObjectAttributeEntity", back_populates="object_attribute_value"
    )
