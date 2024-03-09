# SQL-Alchemy Imports
from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import mapped_column, Mapped, relationship

# Local Backend Import
from .base import Base


class ObjectRelationshipEntity(Base):
    __tablename__ = "object_relationship"

    object_relationship_id = Column(Integer, primary_key=True)
    object_parent_id: Mapped[int] = mapped_column(
        ForeignKey("object.object_id"), nullable=False
    )
    object_child_id: Mapped[int] = mapped_column(
        ForeignKey("object.object_id"), nullable=False
    )
    qualifier_id: Mapped[int] = mapped_column(
        ForeignKey("qualifier.qualifier_id"), nullable=False
    )

    qualifier = relationship("QualifierEntity")
