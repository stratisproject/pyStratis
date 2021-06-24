from pybitcoin import Model
from pybitcoin.types import Address


class BalanceRequest(Model):
    """A request model for the smartcontracts/balance endpoint.

    Args:
        address (Address): The smart contract address.
    """
    address: Address
