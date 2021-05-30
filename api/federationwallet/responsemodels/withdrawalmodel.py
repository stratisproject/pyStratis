from pydantic import Field, conint
from pybitcoin import Address, Model
from pybitcoin.types import Money, uint256


class WithdrawalModel(Model):
    """A WithdrawalModel."""
    trx_id: uint256 = Field(alias='Id')
    deposit_id: uint256 = Field(alias='DepositId')
    amount: Money = Field(alias='Amount')
    paying_to: Address = Field(alias='PayingTo')
    block_height: conint(ge=0) = Field(alias='BlockHeight')
    block_hash: uint256 = Field(alias='BlockHash')
    signature_count: conint(ge=0) = Field(alias='SignatureCount')
    spending_output_details: str = Field(alias='SpendingOutputDetails')
    transfer_status: str = Field(alias='TransferStatus')
