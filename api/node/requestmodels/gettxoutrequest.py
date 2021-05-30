from typing import Optional
from pydantic import Field
from pybitcoin import Model
from pybitcoin.types import uint256


class GetTxOutRequest(Model):
    """A GetTxOutRequest."""
    trxid: uint256
    vout: int = 0
    include_mempool: Optional[bool] = Field(default=True, alias='includeMemPool')
