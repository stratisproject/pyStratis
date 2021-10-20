from pydantic import Field
from pystratis.api import Model
from pystratis.core import DestinationChain


class OwnersRequest(Model):
    """A pydantic model of a owners request."""
    destination_chain: DestinationChain = Field(alias='destinationChain')
    """The destination chain."""
