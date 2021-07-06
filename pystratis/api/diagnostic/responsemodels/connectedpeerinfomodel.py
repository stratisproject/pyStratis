from typing import Optional
from pydantic import Field
from pystratis.api import Model


class ConnectedPeerInfoModel(Model):
    """A pydantic model representing connected peer information."""
    is_connected: bool = Field(alias='isConnected')
    """True if the peer is connected"""
    disconnect_reason: Optional[str] = Field(alias='disconnectReason')
    """The reason for disconnection."""
    state: int
    """The connection state."""
    endpoint: str = Field(alias='endPoint')
    """The peer's endpoint."""
