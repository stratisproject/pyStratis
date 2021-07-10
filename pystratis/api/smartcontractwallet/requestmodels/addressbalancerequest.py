from pystratis.api import Model
from pystratis.core.types import Address


# noinspection PyUnresolvedReferences
class AddressBalanceRequest(Model):
    """A request model for the smartcontractwallet/address-balance request.

    Args:
        address (Address): The smart contract address being queried.
    """
    address: Address
