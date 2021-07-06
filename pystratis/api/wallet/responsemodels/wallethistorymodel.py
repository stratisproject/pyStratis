from typing import List
from pydantic import Field
from pystratis.api import Model
from .accounthistorymodel import AccountHistoryModel


class WalletHistoryModel(Model):
    """A pydantic model for a wallet history."""
    history: List[AccountHistoryModel] = Field(alias='History')
    """A list of account histories."""
