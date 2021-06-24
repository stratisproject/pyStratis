from pybitcoin import Model
from pybitcoin.types import Address


class AddressBalanceRequest(Model):
    """A request model for the smartcontractwallet/address-balance request.

    Args:
        address (Address): The smart contract address being queried.
    """
    address: Address
