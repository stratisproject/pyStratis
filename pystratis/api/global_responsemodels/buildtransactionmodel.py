from typing import Optional
from pydantic import Field
from pystratis.core.types import Money, uint256, hexstr
from pystratis.api import Model


class BuildTransactionModel(Model):
    """A BuildTransactionModel."""
    fee: Optional[Money] = Field(default=0)
    hex: Optional[hexstr]
    transaction_id: Optional[uint256] = Field(alias='transactionId')
