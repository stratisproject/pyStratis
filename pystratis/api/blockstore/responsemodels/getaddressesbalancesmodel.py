from typing import Optional, List
from pystratis.core import Model
from .addressbalancemodel import AddressBalanceModel


class GetAddressesBalancesModel(Model):
    """A GetAddressesBalancesModel."""
    balances: Optional[List[AddressBalanceModel]]
    reason: Optional[str]
