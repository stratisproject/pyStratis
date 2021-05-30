from typing import Any
from pydantic import Field
from pybitcoin import Model


class SerializableResult(Model):
    """A SerializableResult."""
    value: Any
    message: str = Field(default='')
