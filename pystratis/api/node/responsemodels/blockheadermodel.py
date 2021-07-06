from typing import Optional
from pydantic import Field
from datetime import datetime
from pystratis.api import Model
from pystratis.core.types import uint256, hexstr


class BlockHeaderModel(Model):
    """A pydantic model representing the block header."""
    version: int
    """The version of the block."""
    merkleroot: hexstr
    """The merkle root of the block."""
    nonce: int
    """The nonce."""
    bits: str
    """The block's bits."""
    previous_blockhash: Optional[uint256] = Field(alias='previousblockhash')
    """The previous blockhash."""
    time: datetime
    """The time of the block."""
