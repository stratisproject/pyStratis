from pystratis.api import Model
from pystratis.core.types import Address, Money


class AddressBalanceModel(Model):
    """A pydantic model representing an address and balance."""
    address: Address
    """Am address validated on the current network."""
    balance: Money
    """The balance in coin units."""
