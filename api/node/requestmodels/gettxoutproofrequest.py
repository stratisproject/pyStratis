from typing import List, Optional
from pybitcoin import Model
from pybitcoin.types import uint256


class GetTxOutProofRequest(Model):
    """A GetTxOutProofRequest."""
    txids: List[uint256]
    blockhash: Optional[uint256]
