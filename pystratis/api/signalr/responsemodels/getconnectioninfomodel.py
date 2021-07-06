from pydantic import Field
from pystratis.api import Model


class GetConnectionInfoModel(Model):
    """A pydantic model for SignalR connection information."""
    signalr_uri: str = Field(alias='signalRUri')
    """The SignalR uri."""
    signalr_port: int = Field(alias='signalRPort')
    """The SignalR port."""
