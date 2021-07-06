from pydantic import Field
from pystratis.core import CrossChainTransferStatus
from pystratis.api import Model
from pystratis.api.global_responsemodels import TransactionModel
from pystratis.core.types import Money, uint256


class CrossChainTransferModel(Model):
    """A pydantic model of a cross chain transfer."""
    deposit_amount: Money = Field(alias='depositAmount')
    """The amount deposited."""
    deposit_id: uint256 = Field(alias='depositId')
    """The hash of the deposit transaction."""
    deposit_height: int = Field(alias='depositHeight')
    """The height of the deposit transaction."""
    transfer_status: CrossChainTransferStatus = Field(alias='transferStatus')
    """The transfer status."""
    tx: TransactionModel
    """The transaction model of the cross chain transaction."""
