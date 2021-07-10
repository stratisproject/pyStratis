from pystratis.api import Model
from pystratis.core.types import Address


# noinspection PyUnresolvedReferences
class CodeRequest(Model):
    """A request model for the smartcontracts/code endpoint.

    Args:
        address (Address): The smart contract address containing the contract bytecode.
    """
    address: Address
