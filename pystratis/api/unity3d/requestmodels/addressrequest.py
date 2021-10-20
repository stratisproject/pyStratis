from pystratis.api import Model
from pystratis.core.types import Address


# noinspection PyUnresolvedReferences
class AddressRequest(Model):
    """A request model for the unity3d address endpoints.

    Args:
        address (Address): The address.
    """
    address: Address
