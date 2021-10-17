from pydantic import Field
from pystratis.api import Model
from pystratis.core import DestinationChain
from pystratis.core.types import Address


class RemoveOwnerRequest(Model):
    """A pydantic model of a removeowner request."""
    destination_chain: DestinationChain = Field(alias='destinationChain')
    """The destination chain."""
    existing_owner_address: Address = Field(alias='existingOwnerAddress')
    """The existing owner address."""
    gas_price: int = Field(alias='gasPrice')
    """The gas price."""
