from datetime import datetime
from typing import List, Optional
from pydantic import Field
from pystratis.core.types import uint256, hexstr
from pystratis.api import Model


class BlockModel(Model):
    """A pydantic model of a block."""
    hash: uint256
    """The block hash."""
    confirmations: int
    """The number of confirmations."""
    size: int
    """The size of the block."""
    weight: int
    """The weight of the block."""
    height: int
    """The height of the block."""
    version: int
    """The block version."""
    version_hex: str = Field(alias='versionHex')
    """The block version in hex."""
    merkleroot: hexstr
    """The block merkleroot."""
    tx: Optional[List[uint256]]
    """A list of transactions in the block."""
    time: datetime
    """The time the block was produced."""
    median_time: datetime = Field(alias='mediantime')
    """The median time."""
    nonce: int
    """The block's nonce."""
    bits: str
    """The block bits."""
    difficulty: float
    """The block difficulty."""
    chainwork: str
    """The chain work."""
    n_tx: int = Field(alias='nTx')
    """The number of transactions in the block."""
    previous_blockhash: Optional[uint256] = Field(alias='previousblockhash')
    """The previous block hash."""
    next_blockhash: Optional[uint256] = Field(alias='nextblockhash')
    """The next block hash."""
    signature: Optional[str]
    """The signature."""
    modifier_v2: Optional[str] = Field(alias='modifierv2')
    """The block modifier."""
    flags: Optional[str]
    """Block flags."""
    hashproof: Optional[str]
    """Block hashproof."""
    blocktrust: Optional[str]
    """Blocktrust."""
    chaintrust: Optional[str]
    """Chaintrust."""
