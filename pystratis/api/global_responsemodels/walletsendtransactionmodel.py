from typing import List
from pydantic import Field
from pystratis.api import Model
from pystratis.core.types import uint256
from .transactionoutputmodel import TransactionOutputModel


class WalletSendTransactionModel(Model):
    """A WalletSendTransactionModel."""
    transaction_id: uint256 = Field(alias='transactionId')
    outputs: List[TransactionOutputModel]
