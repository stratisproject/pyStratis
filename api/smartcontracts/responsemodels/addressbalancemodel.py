from typing import Optional
from pybitcoin import Model
from pybitcoin.types import Address, Money


class AddressBalanceModel(Model):
    """An AddressBalanceModel."""
    address: Optional[Address]
    sum: Optional[Money]
