from typing import Optional
from pydantic import Field
from pystratis.core import Model


class GetStatusModel(Model):
    """A GetStatusModel."""
    peer_statistics: Optional[str] = Field(alias='peerStatistics')
