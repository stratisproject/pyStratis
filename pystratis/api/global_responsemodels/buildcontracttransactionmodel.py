from typing import Optional
from pydantic import Field
from pystratis.core.types import Money, uint256, hexstr
from pystratis.api import Model


class BuildContractTransactionModel(Model):
    """A BuildContractTransactionModel."""
    fee: Optional[Money]
    hex: Optional[hexstr]
    message: Optional[str]
    success: Optional[bool]
    transaction_id: Optional[uint256] = Field(alias='transactionId')
