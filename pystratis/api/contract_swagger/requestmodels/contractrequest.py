from pystratis.api import Model
from pystratis.core.types import Address


# noinspection PyUnresolvedReferences
class ContractRequest(Model):
    """A request model for the swagger/contract endpoint.

    Args:
        address (Address): The address.
    """
    address: Address
