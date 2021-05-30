from pydantic import Field
from pybitcoin import Model


class DisconnectPeerRequest(Model):
    """A DisconnectPeerRequest."""
    peer_address: str = Field(alias='peerAddress')
