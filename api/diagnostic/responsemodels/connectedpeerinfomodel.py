from typing import Optional
from pydantic import Field, conint
from pybitcoin import Model


class ConnectedPeerInfoModel(Model):
    """A ConnectedPeerInfoModel."""
    is_connected: bool = Field(alias='isConnected')
    disconnect_reason: Optional[str] = Field(alias='disconnectReason')
    state: conint(ge=0)
    endpoint: str = Field(alias='endPoint')
