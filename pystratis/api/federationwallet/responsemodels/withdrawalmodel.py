from typing import Union, Optional
from pydantic import Field, conint
from pystratis.core.types import Address
from pystratis.core import CrossChainTransferStatus, Model
from pystratis.core.types import Money, uint256


class WithdrawalModel(Model):
    """A WithdrawalModel."""
    trx_id: Optional[uint256] = Field(alias='id')
    deposit_id: Optional[uint256] = Field(alias='depositId')
    amount: Optional[Money] = Field(alias='amount')
    paying_to: Optional[Union[str, Address]] = Field(alias='payingTo')
    block_height: Optional[conint(ge=0)] = Field(alias='blockHeight')
    block_hash: Optional[uint256] = Field(alias='blockHash')
    signature_count: Optional[conint(ge=0)] = Field(alias='signatureCount')
    spending_output_details: Optional[str] = Field(alias='spendingOutputDetails')
    transfer_status: Optional[CrossChainTransferStatus] = Field(alias='transferStatus')
