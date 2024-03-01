# Local Backend Imports
from .camel_model import CamelModel


class RequestModel(CamelModel):
    event_id: int
    event_type_id: int
    timestamp: str
    event_attribute_id: int
    event_attribute_value_id: int
    object_id: int
    object_attribute_id: int
    object_attribute_value_id: int
    qualifier_id: int


class EventTypeModel(CamelModel):
    name: str | None = ""
