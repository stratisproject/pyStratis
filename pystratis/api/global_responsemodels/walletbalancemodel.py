from typing import List
from pystratis.api import Model
from .accountbalancemodel import AccountBalanceModel


class WalletBalanceModel(Model):
    """A WalletBalanceModel."""
    balances: List[AccountBalanceModel]
