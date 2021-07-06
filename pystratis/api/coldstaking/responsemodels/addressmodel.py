from pystratis.api import Model
from pystratis.core.types import Address


class AddressModel(Model):
    """A pydantic model for a cold staking address."""
    address: Address
    """The cold staking address."""
