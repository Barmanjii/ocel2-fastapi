# SQL-Alchemy Imports
from sqlalchemy import Column, JSON, Integer

# Local Backend Import
from .base import Base


class qualifierEntity(Base):
    __tablename__ = "qualifier"

    qualifier_id = Column(Integer, primary_key=True)
    value = Column(JSON, default={})
