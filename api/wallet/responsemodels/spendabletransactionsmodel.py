from typing import List
from pybitcoin import Model
from .spendabletransactionmodel import SpendableTransactionModel


class SpendableTransactionsModel(Model):
    """A SpendableTransactionsModel."""
    transactions: List[SpendableTransactionModel]
