from typing import Any, Optional
from pydantic import Field
from pybitcoin import Model


class SerializableResult(Model):
    """A SerializableResult."""
    value: Optional[Any]
    message: Optional[str] = Field(default='')
