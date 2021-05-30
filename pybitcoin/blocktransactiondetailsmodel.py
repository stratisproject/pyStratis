from typing import List
from pydantic import Field
from .blockmodel import BlockModel
from .transactionmodel import TransactionModel


class BlockTransactionDetailsModel(BlockModel):
    """A BlockTransactionDetailsModel."""
    transactions: List[TransactionModel] = Field(alias='Transactions')
