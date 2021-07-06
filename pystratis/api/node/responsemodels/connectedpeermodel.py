from pydantic import Field
from pystratis.api import Model


class ConnectedPeerModel(Model):
    """A  pydantic model representing a connected peer."""
    version: str
    """The connectedpeer's version."""
    remote_socket_endpoint: str = Field(alias='remoteSocketEndpoint')
    """The connected peer's remote socket endpoint."""
    tip_height: int = Field(alias='tipHeight')
    """The connected peer's tip height."""
