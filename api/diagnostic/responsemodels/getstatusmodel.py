from pydantic import Field
from pybitcoin import Model


class GetStatusModel(Model):
    """A GetStatusModel."""
    peer_statistics: str = Field(alias='peerStatistics')
