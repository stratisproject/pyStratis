from typing import List, Optional
from pydantic import Field
from pystratis.api import Model
from pystratis.core.types import uint256


# noinspection PyUnresolvedReferences
class GetTxOutProofRequest(Model):
    """A request model for the node/gettxoutproof endpoint.
    Args:
        txids (List[uint256]): A list of transaction hashes.
        block_hash (uint256, optional): The block hash to check.
    """
    txids: List[uint256]
    block_hash: Optional[uint256] = Field(alias='blockhash')
