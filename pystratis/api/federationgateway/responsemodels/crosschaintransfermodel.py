from typing import Optional
from pydantic import Field, conint
from pystratis.core import CrossChainTransferStatus, Model, TransactionModel
from pystratis.core.types import Money, uint256


class CrossChainTransferModel(Model):
    """A CrossChainTransferModel."""
    deposit_amount: Optional[Money] = Field(alias='depositAmount')
    deposit_id: Optional[uint256] = Field(alias='depositId')
    deposit_height: Optional[conint(ge=0)] = Field(alias='depositHeight')
    transfer_status: Optional[CrossChainTransferStatus] = Field(alias='transferStatus')
    tx: Optional[TransactionModel]
