from typing import Union
from pydantic import Field
from pystratis.core.types import Address
from pystratis.core import CrossChainTransferStatus
from pystratis.api import Model
from pystratis.core.types import Money, uint256


class WithdrawalModel(Model):
    """A pydantic model for a withdrawal processed by the multisig federation."""
    trx_id: uint256 = Field(alias='id')
    """The transaction hash."""
    deposit_id: uint256 = Field(alias='depositId')
    """The deposit transaction hash."""
    amount: Money = Field(alias='amount')
    """The amount of the withdrawal."""
    paying_to: Union[str, Address] = Field(alias='payingTo')
    """The address receiving the withdrawal."""
    block_height: int = Field(alias='blockHeight')
    """The block height of the withdrawal."""
    block_hash: uint256 = Field(alias='blockHash')
    """The hash of the block containing the withdrawal."""
    signature_count: int = Field(alias='signatureCount')
    """The number of signatures on the withdrawal."""
    spending_output_details: str = Field(alias='spendingOutputDetails')
    """Spending output details."""
    transfer_status: CrossChainTransferStatus = Field(alias='transferStatus')
    """The cross chain transfer status."""
