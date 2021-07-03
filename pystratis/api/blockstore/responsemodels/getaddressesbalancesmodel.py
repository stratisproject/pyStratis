from typing import Optional, List
from pystratis.api import Model
from .addressbalancemodel import AddressBalanceModel


class GetAddressesBalancesModel(Model):
    """A GetAddressesBalancesModel."""
    balances: Optional[List[AddressBalanceModel]]
    reason: Optional[str]
