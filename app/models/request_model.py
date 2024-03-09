# Pydantic Import
from datetime import datetime
from pydantic import BaseModel
from typing import List


class EventAttribute(BaseModel):
    name: str


class EventAttributeValue(BaseModel):
    value: dict


class Qualifier(BaseModel):
    value: dict


class Event(BaseModel):
    timestamp: datetime
    attribute_values: List[EventAttributeValue]
    relationships: List[Qualifier]


class EventType(BaseModel):
    name: str
    attributes: List[EventAttribute]


class ObjectAttribute(BaseModel):
    name: str


class ObjectType(BaseModel):
    name: str
    attributes: List[ObjectAttribute]


class ObjectAttributeValue(BaseModel):
    timestamp: datetime
    value: dict


class RequestModel(BaseModel):
    event_types: List[EventType]
    object_types: List[ObjectType]
    events: List[Event]
    objects: List[ObjectAttributeValue]
