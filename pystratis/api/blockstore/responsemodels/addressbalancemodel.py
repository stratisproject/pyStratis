from typing import Optional
from pystratis.core import Model
from pystratis.core.types import Address, Money


class AddressBalanceModel(Model):
    """A AddressBalanceModel."""
    address: Optional[Address]
    balance: Optional[Money]
