# SQL-Alchemy Imports
from sqlalchemy import Column, JSON, Integer

# Local Backend Import
from .base import Base


class QualiferEntity(Base):
    __tablename__ = "qualifer"

    qualifer_id = Column(Integer, primary_key=True)
    value = Column(JSON, default={})
