from typing import List, Optional
from pybitcoin import Model
from pybitcoin.types import uint256


class GenerateBlocksModel(Model):
    """A GenerateBlocksModel."""
    blocks: Optional[List[uint256]]
