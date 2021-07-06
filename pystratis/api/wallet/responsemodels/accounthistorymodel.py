from typing import List
from pydantic import Field
from pystratis.api import Model
from pystratis.core import CoinType
from .transactionitemmodel import TransactionItemModel


class AccountHistoryModel(Model):
    """An pydantic model for account history."""
    account_name: str = Field(alias='accountName')
    """The account name."""
    account_hd_path: str = Field(alias='accountHdPath')
    """The account HD path."""
    coin_type: CoinType = Field(alias='coinType')
    """The coin type."""
    transactions_history: List[TransactionItemModel] = Field(alias='transactionsHistory')
    """A list of transactions composing the history."""
