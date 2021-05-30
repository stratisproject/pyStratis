from typing import List
from pydantic import Field, conint
from pybitcoin import Model


class PeerStatisticsModel(Model):
    """A PeerStatisticsModel."""
    peer_endpoint: str = Field(alias='peerEndPoint')
    connected: bool
    inbound: bool
    bytes_sent: conint(ge=0) = Field(alias='bytesSent')
    bytes_received: conint(ge=0) = Field(alias='bytesReceived')
    received_messages: conint(ge=0) = Field(alias='receivedMessages')
    send_messages: conint(ge=0) = Field(alias='sentMessages')
    latest_events: List[str] = Field(alias='latestEvents')
