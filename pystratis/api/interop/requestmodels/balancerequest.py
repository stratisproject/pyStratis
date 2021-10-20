from pydantic import Field
from pystratis.api import Model
from pystratis.core import DestinationChain
from pystratis.core.types import Address


class BalanceRequest(Model):
    """A pydantic model of a balance request."""
    destination_chain: DestinationChain = Field(alias='destinationChain')
    """The destination chain."""
    account: str
    """The account id."""
