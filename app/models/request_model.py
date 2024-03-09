# Pydantic Import
from datetime import datetime
from pydantic import BaseModel


# class RequestModel(BaseModel):
#     event_type_name: str | None = ""
#     event_attribute_name: str | None = ""
#     event_attribute_value_value: dict | None = {}

#     object_type_name: str | None = ""
#     object_attribute_name: str | None = ""
#     object_attribute_value_value: dict | None = {}

#     qualifier_value: dict | None = {}


class Event(BaseModel):
    timestamp: datetime


class EventType(BaseModel):
    name: str


class EventAttributeEntity(BaseModel):
    name: str


class EventAttributeValueEntity(BaseModel):
    value: dict


class RequestModel(BaseModel):
    event: Event
    event_type: EventType
    event_attribute: EventAttributeEntity
    event_attribute_value: EventAttributeValueEntity
