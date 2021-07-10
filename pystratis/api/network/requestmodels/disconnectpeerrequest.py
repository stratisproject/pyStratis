from pydantic import Field
from pystratis.api import Model


# noinspection PyUnresolvedReferences
class DisconnectPeerRequest(Model):
    """A request model for the network/disconnect endpoint.

    Args:
        peer_address (str): The peer endpoint.
    """
    peer_address: str = Field(alias='peerAddress')
