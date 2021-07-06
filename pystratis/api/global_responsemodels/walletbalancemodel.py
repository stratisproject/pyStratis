from typing import List
from pystratis.api import Model
from .accountbalancemodel import AccountBalanceModel


class WalletBalanceModel(Model):
    """A pydantic model for a wallet balance."""
    balances: List[AccountBalanceModel]
    """A list of account balances."""
