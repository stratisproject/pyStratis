from pydantic import Field
from pystratis.api import Model
from pystratis.core.types import Address


# noinspection PyUnresolvedReferences
class ReceivedByAddressRequest(Model):
    """A request model for the wallet/received-by-address endpoint.

    Args:
        address (Address): The address to query.
    """
    address: Address = Field(alias='Address')
