from typing import List, Optional
from pystratis.core import Model
from .spendabletransactionmodel import SpendableTransactionModel


class SpendableTransactionsModel(Model):
    """A SpendableTransactionsModel."""
    transactions: Optional[List[SpendableTransactionModel]]
