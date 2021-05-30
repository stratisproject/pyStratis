from typing import Optional, List
from pybitcoin import Model
from .addressbalancemodel import AddressBalanceModel


class GetAddressesBalancesModel(Model):
    """A GetAddressesBalancesModel."""
    balances: List[AddressBalanceModel]
    reason: Optional[str]
