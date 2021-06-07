from typing import Optional
from pybitcoin import Address, Model
from pybitcoin.types import Money


class AddressBalanceModel(Model):
    """A AddressBalanceModel."""
    address: Optional[Address]
    balance: Optional[Money]
