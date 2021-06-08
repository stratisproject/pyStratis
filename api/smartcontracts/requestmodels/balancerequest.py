from pybitcoin import Model
from pybitcoin.types import Address


class BalanceRequest(Model):
    """A BalanceRequest."""
    address: Address
