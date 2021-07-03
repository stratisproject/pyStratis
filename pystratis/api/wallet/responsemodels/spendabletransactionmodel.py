from typing import Optional
from pydantic import Field, conint
from pystratis.core import Model
from pystratis.core.types import Address, Money, uint256
from datetime import datetime


class SpendableTransactionModel(Model):
    """A SpendableTransactionModel."""
    transaction_id: Optional[uint256] = Field(alias='id')
    index: Optional[conint(ge=0)]
    address: Optional[Address]
    is_change: Optional[bool] = Field(alias='isChange')
    amount: Optional[Money]
    creation_time: Optional[datetime] = Field(alias='creationTime')
    confirmations: Optional[conint(ge=0)]
