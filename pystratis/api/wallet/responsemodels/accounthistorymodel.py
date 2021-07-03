from typing import List, Optional
from pydantic import Field
from pystratis.core import Model, CoinType
from .transactionitemmodel import TransactionItemModel


class AccountHistoryModel(Model):
    """An AccountHistoryModel"""
    account_name: Optional[str] = Field(alias='accountName')
    account_hd_path: Optional[str] = Field(alias='accountHdPath')
    coin_type: Optional[CoinType] = Field(alias='coinType')
    transactions_history: Optional[List[TransactionItemModel]] = Field(alias='transactionsHistory')
