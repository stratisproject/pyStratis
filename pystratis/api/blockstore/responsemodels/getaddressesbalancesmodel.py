from typing import Optional, List
from pystratis.api import Model
from .addressbalancemodel import AddressBalanceModel


class GetAddressesBalancesModel(Model):
    """A pydantic model for retrieving multiple address balances."""
    balances: List[AddressBalanceModel]
    """A list of addresses with current balances."""
    reason: Optional[str]
    """If query failed, a reason is given."""
