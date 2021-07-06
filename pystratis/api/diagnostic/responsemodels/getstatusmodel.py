from pydantic import Field
from pystratis.api import Model


class GetStatusModel(Model):
    """A pydantic model for status of diagnostics collection service."""
    peer_statistics: str = Field(alias='peerStatistics')
    """The status of the service."""
