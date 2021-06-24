from pybitcoin import Model
from pybitcoin.types import Address


class CodeRequest(Model):
    """A request model for the smartcontracts/code endpoint.

    Args:
        address (Address): The smart contract address containing the contract bytecode.
    """
    address: Address
