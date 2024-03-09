# SQL-Alchemy Imports
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import mapped_column, Mapped, relationship

# Local Backend Import
from .base import Base


class ObjectAttributeEntity(Base):
    __tablename__ = "object_attribute"

    object_attribute_id = Column(Integer, primary_key=True)
    object_type_id = Column(ForeignKey("object_type.object_type_id"), nullable=False)
    name = Column(String(255), default="")
    object_type: Mapped["ObjectTypeEntity"] = relationship(
        back_populates="object_attribute"
    )
    object_attribute_value = relationship("ObjectAttributeValueEntity")
