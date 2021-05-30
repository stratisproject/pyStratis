from typing import List
from pydantic import Field
from pybitcoin import Model
from .accounthistorymodel import AccountHistoryModel


class WalletHistoryModel(Model):
    """A WalletHistoryModel."""
    history: List[AccountHistoryModel] = Field(alias='History')
