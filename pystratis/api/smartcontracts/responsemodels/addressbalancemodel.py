from pystratis.api import Model
from pystratis.core.types import Address, Money


class AddressBalanceModel(Model):
    """A pydantic model for an address balance."""
    address: Address
    """The address."""
    sum: Money
    """The amount present at the address."""
