from typing import List
from pybitcoin import Model
from pybitcoin.types import uint256


class GenerateBlocksModel(Model):
    """A GenerateBlocksModel."""
    blocks: List[uint256]
