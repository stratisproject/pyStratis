from typing import Optional
from pydantic import Field, conint
from pybitcoin import Address, Model
from pybitcoin.types import Money, uint256


class SpendableTransactionModel(Model):
    """A SpendableTransactionModel."""
    transaction_id: Optional[uint256] = Field(alias='id')
    index: Optional[conint(ge=0)]
    address: Optional[Address]
    is_change: Optional[bool] = Field(alias='isChange')
    amount: Optional[Money]
    creation_time: Optional[str] = Field(alias='creationTime')
    confirmations: Optional[conint(ge=0)]
