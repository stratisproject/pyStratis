from typing import List
from pybitcoin import Address, Model
from pydantic import Field
from .balancechangesmodel import BalanceChangesModel


class VerboseAddressBalanceModel(Model):
    """A VerboseAddressBalanceModel."""
    address: Address
    balance_changes: List[BalanceChangesModel] = Field(alias='balanceChanges')
