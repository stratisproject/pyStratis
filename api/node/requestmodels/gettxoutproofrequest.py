from typing import List, Optional
from pybitcoin import Model
from pybitcoin.types import uint256


class GetTxOutProofRequest(Model):
    """A GetTxOutProofRequest."""
    txids: List[uint256]
    block_hash: Optional[uint256]
