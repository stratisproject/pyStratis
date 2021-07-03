from datetime import datetime
from typing import List, Optional
from pydantic import Field
from pystratis.core.types import uint256
from pystratis.api import Model


class BlockModel(Model):
    """A BlockModel."""
    hash: uint256
    confirmations: int
    size: int
    weight: int
    height: int
    version: int
    version_hex: str = Field(alias='versionHex')
    merkleroot: str
    tx: Optional[List[uint256]]
    time: datetime
    median_time: datetime = Field(alias='mediantime')
    nonce: int
    bits: str
    difficulty: float
    chainwork: str
    n_tx: int = Field(alias='nTx')
    previous_blockhash: uint256 = Field(alias='previousblockhash')
    next_blockhash: Optional[uint256] = Field(alias='nextblockhash')
    signature: Optional[str]
    modifier_v2: Optional[str] = Field(alias='modifierv2')
    flags: Optional[str]
    hashproof: Optional[str]
    blocktrust: Optional[str]
    chaintrust: Optional[str]
