from pydantic import Field
from pystratis.api import Model


class SetOriginatorRequest(Model):
    """A pydantic model of a setoriginator request."""
    request_id: int = Field(alias='requestId')
    """The request id."""
