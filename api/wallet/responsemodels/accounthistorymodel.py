from typing import List
from pydantic import Field
from pybitcoin import Model, CoinType
from .transactionitemmodel import TransactionItemModel


class AccountHistoryModel(Model):
    """An AccountHistoryModel"""
    account_name: str = Field(alias='accountName')
    account_hd_path: str = Field(alias='accountHdPath')
    coin_type: CoinType = Field(alias='coinType')
    transactions_history: List[TransactionItemModel] = Field(alias='transactionsHistory')
