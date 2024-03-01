# SQL-Alchemy Imports
from sqlalchemy.sql import func
from sqlalchemy.dialects import postgresql as pg
from sqlalchemy import Column, ForeignKey, Integer, JSON

# Local Backend Import
from .base import Base


class ObjectRelationshipEntity(Base):
    __tablename__ = "object_relationship"

    object_relationship_id = Column(Integer, primary_key=True)
    object_parent_id = Column(ForeignKey("object.object_id"), nullable=False)
    object_child_id = Column(ForeignKey("object.object_id"), nullable=False)
    qualifer_id = Column(ForeignKey("qualifer.qualifer_id"), nullable=False)
