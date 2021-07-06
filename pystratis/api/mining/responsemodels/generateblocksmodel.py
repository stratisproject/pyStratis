from typing import List
from pystratis.api import Model
from pystratis.core.types import uint256


class GenerateBlocksModel(Model):
    """A pydantic model for generated blocks."""
    blocks: List[uint256]
    """A list of hashes of generated blocks."""
