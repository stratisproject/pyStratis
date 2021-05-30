from pydantic import Field, conint
from pybitcoin import Model


class ConnectedPeerModel(Model):
    """A ConnectedPeerModel."""
    version: str
    remote_socket_endpoint: str = Field(alias='remoteSocketEndpoint')
    tip_height: conint(ge=0) = Field(alias='tipHeight')
