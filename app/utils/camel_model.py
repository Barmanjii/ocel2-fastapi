# Main Python Import
from pydantic import ConfigDict, BaseModel

# Local Backend Import
from app.utils.model_utils import camelize_for_request


def to_camel(string):
    return camelize_for_request(string)


class CamelModel(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)
