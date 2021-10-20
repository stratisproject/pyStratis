from pydantic import Field
from pystratis.api import Model
from pystratis.core import DestinationChain
from pystratis.core.types import Address


class AddOwnerRequest(Model):
    """A pydantic model of a addowner request."""
    destination_chain: DestinationChain = Field(alias='destinationChain')
    """The destination chain."""
    new_owner_address: Address = Field(alias='newOwnerAddress')
    """The new owner address."""
    gas_price: int = Field(alias='gasPrice')
    """The gas price."""
