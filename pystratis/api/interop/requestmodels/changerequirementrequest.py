from pydantic import Field
from pystratis.api import Model
from pystratis.core import DestinationChain
from pystratis.core.types import Address


class ChangeRequirementRequest(Model):
    """A pydantic model of a changerequirement request."""
    destination_chain: DestinationChain = Field(alias='destinationChain')
    """The destination chain."""
    requirement: int
    """The new threshold of confirmations."""
    gas_price: int = Field(alias='gasPrice')
    """The gas price."""
