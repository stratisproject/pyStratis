from typing import Optional
from pydantic import Field, conint
from pybitcoin import Address, CrossChainTransferStatus, Model
from pybitcoin.types import Money, uint256


class WithdrawalModel(Model):
    """A WithdrawalModel."""
    trx_id: Optional[uint256] = Field(alias='Id')
    deposit_id: Optional[uint256] = Field(alias='DepositId')
    amount: Optional[Money] = Field(alias='Amount')
    paying_to: Optional[Address] = Field(alias='PayingTo')
    block_height: Optional[conint(ge=0)] = Field(alias='BlockHeight')
    block_hash: Optional[uint256] = Field(alias='BlockHash')
    signature_count: Optional[conint(ge=0)] = Field(alias='SignatureCount')
    spending_output_details: Optional[str] = Field(alias='SpendingOutputDetails')
    transfer_status: Optional[CrossChainTransferStatus] = Field(alias='TransferStatus')
