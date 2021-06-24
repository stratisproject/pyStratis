from pydantic import Field
from pybitcoin import Model
from pybitcoin.types import Address


class ReceivedByAddressRequest(Model):
    """A request model for the wallet/received-by-address endpoint.

    Args:
        address (Address): The address to query.
    """
    address: Address = Field(alias='Address')
