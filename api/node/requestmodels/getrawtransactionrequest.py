from typing import Optional
from pybitcoin import Model
from pybitcoin.types import uint256


class GetRawTransactionRequest(Model):
    """A GetRawTransactionRequest."""
    trxid: uint256
    verbose: Optional[bool] = False
