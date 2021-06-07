from typing import List, Optional
from pydantic import Field
from pybitcoin import Model
from .accounthistorymodel import AccountHistoryModel


class WalletHistoryModel(Model):
    """A WalletHistoryModel."""
    history: Optional[List[AccountHistoryModel]] = Field(alias='History')
