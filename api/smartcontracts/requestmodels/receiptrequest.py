from pydantic import Field
from pybitcoin import Model
from pybitcoin.types import uint256


class ReceiptRequest(Model):
    """A ReceiptRequest."""
    tx_hash: uint256 = Field(alias='txHash')
