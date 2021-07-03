from typing import Optional
from pystratis.api import Model
from pystratis.core.types import Address, Money


class AddressBalanceModel(Model):
    """An AddressBalanceModel."""
    address: Optional[Address]
    sum: Optional[Money]
