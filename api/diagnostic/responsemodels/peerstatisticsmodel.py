from typing import List, Optional
from pydantic import Field, conint
from pybitcoin import Model


class PeerStatisticsModel(Model):
    """A PeerStatisticsModel."""
    peer_endpoint: Optional[str] = Field(alias='peerEndPoint')
    connected: Optional[bool]
    inbound: Optional[bool]
    bytes_sent: Optional[conint(ge=0)] = Field(alias='bytesSent')
    bytes_received: Optional[conint(ge=0)] = Field(alias='bytesReceived')
    received_messages: Optional[conint(ge=0)] = Field(alias='receivedMessages')
    send_messages: Optional[conint(ge=0)] = Field(alias='sentMessages')
    latest_events: Optional[List[str]] = Field(alias='latestEvents')
