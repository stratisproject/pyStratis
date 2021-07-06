from pydantic import Field
from pystratis.api import Model


class BannedPeerModel(Model):
    """A pydantic model describing a banned peer."""
    endpoint: str = Field(alias='endPoint')
    """The banned peer endpoint."""
    ban_until: str = Field(alias='banUntil')
    """The time when ban end."""
    ban_reason: str = Field(alias='banReason')
    """The reason for the ban."""
