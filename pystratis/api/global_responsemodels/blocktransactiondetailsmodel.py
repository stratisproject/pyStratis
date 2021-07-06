from typing import List
from pydantic import Field
from .blockmodel import BlockModel
from .transactionmodel import TransactionModel


class BlockTransactionDetailsModel(BlockModel):
    """A pydantic model for block transaction details."""
    transactions: List[TransactionModel] = Field(alias='Transactions')
    """A list of transactions."""
