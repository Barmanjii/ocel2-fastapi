# Pydantic Import
from datetime import datetime

# Main Python Import
from typing import List

# Local Python Import
from app.utils.camel_model import CamelModel


class EventAttribute(CamelModel):
    name: str


class EventAttributeValue(CamelModel):
    value: dict


class Qualifier(CamelModel):
    value: dict


class Event(CamelModel):
    timestamp: datetime
    attribute_values: List[EventAttributeValue]
    relationships_qualifer: List[Qualifier]


class EventType(CamelModel):
    name: str
    attributes: List[EventAttribute]


class ObjectAttribute(CamelModel):
    name: str


class ObjectType(CamelModel):
    name: str
    attributes: List[ObjectAttribute]


class ObjectAttributeValue(CamelModel):
    timestamp: datetime
    value: dict


class RequestModel(CamelModel):
    event_types: List[EventType]
    object_types: List[ObjectType]
    events: List[Event]
    objects: List[ObjectAttributeValue]
