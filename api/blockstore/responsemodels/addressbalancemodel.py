from typing import Optional
from pybitcoin import Model
from pybitcoin.types import Address, Money


class AddressBalanceModel(Model):
    """A AddressBalanceModel."""
    address: Optional[Address]
    balance: Optional[Money]
