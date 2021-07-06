from typing import Any, Optional
from pydantic import Field
from pystratis.api import Model


class SerializableResult(Model):
    """A pydantic model for a serializable result."""
    value: Optional[Any]
    message: Optional[str] = Field(default='')
