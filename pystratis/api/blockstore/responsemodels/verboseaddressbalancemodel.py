from typing import List
from pystratis.api import Model
from pystratis.core.types import Address
from pydantic import Field
from .balancechangesmodel import BalanceChangesModel


class VerboseAddressBalanceModel(Model):
    """A pydantic model that verbosely lists balance changes for a given address."""
    address: Address
    """The given address."""
    balance_changes: List[BalanceChangesModel] = Field(alias='balanceChanges')
    """A list of balance changes for the given address."""
