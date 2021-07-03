from typing import List, Optional
from pystratis.api import Model
from .spendabletransactionmodel import SpendableTransactionModel


class SpendableTransactionsModel(Model):
    """A SpendableTransactionsModel."""
    transactions: Optional[List[SpendableTransactionModel]]
