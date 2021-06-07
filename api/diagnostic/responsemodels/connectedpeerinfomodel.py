from typing import Optional
from pydantic import Field, conint
from pybitcoin import Model


class ConnectedPeerInfoModel(Model):
    """A ConnectedPeerInfoModel."""
    is_connected: Optional[bool] = Field(alias='isConnected')
    disconnect_reason: Optional[str] = Field(alias='disconnectReason')
    state: Optional[conint(ge=0)]
    endpoint: Optional[str] = Field(alias='endPoint')
