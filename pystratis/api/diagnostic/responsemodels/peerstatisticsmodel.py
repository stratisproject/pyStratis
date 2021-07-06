from typing import List
from pydantic import Field
from pystratis.api import Model


class PeerStatisticsModel(Model):
    """A pydantic model for peer statistics."""
    peer_endpoint: str = Field(alias='peerEndPoint')
    """The peer endpoint."""
    connected: bool
    """If true, peer is connected."""
    inbound: bool
    """If true, peer is inbound connection."""
    bytes_sent: int = Field(alias='bytesSent')
    """Bytes sent to peer."""
    bytes_received: int = Field(alias='bytesReceived')
    """Bytes received from peer."""
    received_messages: int = Field(alias='receivedMessages')
    """The number of received messages from peer."""
    send_messages: int = Field(alias='sentMessages')
    """The number of sent  messages to peer."""
    latest_events: List[str] = Field(alias='latestEvents')
    """A list of peer events."""
