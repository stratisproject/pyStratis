from typing import Optional
from pydantic import Field, conint
from pystratis.api import Model


class ConnectedPeerModel(Model):
    """A ConnectedPeerModel."""
    version: Optional[str]
    remote_socket_endpoint: Optional[str] = Field(alias='remoteSocketEndpoint')
    tip_height: Optional[conint(ge=0)] = Field(alias='tipHeight')
