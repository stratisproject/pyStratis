from typing import List, Optional
from pystratis.core import Model
from pystratis.core.types import uint256


class GenerateBlocksModel(Model):
    """A GenerateBlocksModel."""
    blocks: Optional[List[uint256]]
