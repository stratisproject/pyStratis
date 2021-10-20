from pydantic import Field
from pystratis.api import Model


class ReprocessBurnRequest(Model):
    """A pydantic model of a reprocess burn request."""
    request_id: int = Field(alias='id')
    """The request id to reprocess."""
    height: int
    """The height at which to reprocess the burn."""
