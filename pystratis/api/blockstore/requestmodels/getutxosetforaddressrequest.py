from pystratis.api import Model
from pystratis.core.types import Address


class GetUTXOSetForAddressRequest(Model):
    """A request model for the GetUTXOSetForAddressRequest.

    Args:
        address (int): The address.
    """
    address: Address
