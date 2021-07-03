from typing import Optional, List
from pystratis.api import Model
from pystratis.core.types import Address
from pydantic import Field
from .balancechangesmodel import BalanceChangesModel


class VerboseAddressBalanceModel(Model):
    """A VerboseAddressBalanceModel."""
    address: Optional[Address]
    balance_changes: Optional[List[BalanceChangesModel]] = Field(alias='balanceChanges')
