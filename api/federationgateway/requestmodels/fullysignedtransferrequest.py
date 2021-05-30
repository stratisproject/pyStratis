from pydantic import Field
from pybitcoin import Model
from pybitcoin.types import uint256


class FullySignedTransferRequest(Model):
    """A FullySignedTransferRequest."""
    deposit_id: uint256 = Field(alias='depositId')
    transaction_id: uint256 = Field(alias='transactionId')
