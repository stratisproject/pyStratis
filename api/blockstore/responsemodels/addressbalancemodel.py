from pybitcoin import Address, Model
from pybitcoin.types import Money


class AddressBalanceModel(Model):
    """A AddressBalanceModel."""
    address: Address
    balance: Money
