from typing import List
from pystratis.api import Model
from .spendabletransactionmodel import SpendableTransactionModel


class SpendableTransactionsModel(Model):
    """A pydantic model for a list of spendable transactions."""
    transactions: List[SpendableTransactionModel]
    """A list of spendable transactions."""
