from typing import Optional
from pydantic import Field
from pystratis.core.types import Money, uint256, hexstr
from pystratis.api import Model


class BuildContractTransactionModel(Model):
    """A pydantic model for building a smart contact transaction."""
    fee: Money
    """The transaction fee."""
    hex: hexstr
    """The hex serialized transaction."""
    message: Optional[str]
    """The build transaction message."""
    success: Optional[bool]
    """True if build was successful."""
    transaction_id: Optional[uint256] = Field(alias='transactionId')
    """The transaction hash, if build successful."""
