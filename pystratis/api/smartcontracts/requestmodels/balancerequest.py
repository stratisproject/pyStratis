from pystratis.api import Model
from pystratis.core.types import Address


# noinspection PyUnresolvedReferences
class BalanceRequest(Model):
    """A request model for the smartcontracts/balance endpoint.

    Args:
        address (Address): The smart contract address.
    """
    address: Address
