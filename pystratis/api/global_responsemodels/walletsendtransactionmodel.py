from typing import List
from pydantic import Field
from pystratis.api import Model
from pystratis.core.types import uint256
from .transactionoutputmodel import TransactionOutputModel


class WalletSendTransactionModel(Model):
    """A pydantic model for a send transaction response."""
    transaction_id: uint256 = Field(alias='transactionId')
    """The transaction hash."""
    outputs: List[TransactionOutputModel]
    """A list of transaction outputs."""
