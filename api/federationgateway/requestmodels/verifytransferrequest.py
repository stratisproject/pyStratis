from pydantic import Field
from pybitcoin import Model
from pybitcoin.types import uint256


class VerifyTransferRequest(Model):
    """A VerifyTransferRequest."""
    deposit_id_transaction_id: uint256 = Field(alias='depositIdTransactionId')
