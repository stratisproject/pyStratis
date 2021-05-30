from pydantic import Field
from pybitcoin import Model
from pybitcoin.types import uint256


class PendingTransferRequest(Model):
    """A PendingTransferRequest."""
    deposit_id: uint256 = Field(alias='depositId')
    transaction_id: uint256 = Field(alias='transactionId')
