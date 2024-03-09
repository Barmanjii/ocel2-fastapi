# Main Python Import
from typing import List

# SQL-Alchemy Imports
from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.entity.object_relationship import ObjectRelationshipEntity


# Local Backend Import
from .base import Base


class ObjectEntity(Base):
    __tablename__ = "object"

    object_id = Column(Integer, primary_key=True)
    object_type_id: Mapped[int] = mapped_column(
        ForeignKey("object_type.object_type_id"), nullable=False
    )
    object_type: Mapped["ObjectTypeEntity"] = relationship(back_populates="object")
    object_attribute_value = relationship("ObjectAttributeValueEntity")
    parent_relationships = relationship(
        "ObjectRelationshipEntity",
        foreign_keys=[ObjectRelationshipEntity.object_parent_id],
        backref="parent_object",
    )
    child_relationships = relationship(
        "ObjectRelationshipEntity",
        foreign_keys=[ObjectRelationshipEntity.object_child_id],
        backref="child_object",
    )
