from pydantic import Field
from pybitcoin import Model


class GetPeerStatisticsRequest(Model):
    """A GetPeerStatisticsRequest."""
    connected_only: bool = Field(alias='connectedOnly')
