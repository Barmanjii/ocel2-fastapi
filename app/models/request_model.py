# Pydantic Import
from pydantic import BaseModel


class RequestModel(BaseModel):
    event_type_name: str | None = ""
    event_attribute_name: str | None = ""
    event_attribute_value_value: dict | None = {}

    object_type_name: str | None = ""
    object_attribute_name: str | None = ""
    object_attribute_value_value: dict | None = {}

    qualifier_value: dict | None = {}
