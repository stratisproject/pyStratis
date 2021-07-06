from typing import List, Optional
from datetime import datetime
from pystratis.core.types import uint256, hexstr
from pystratis.api import Model
from .vin import VIn
from .vout import VOut


class TransactionModel(Model):
    """A pydantic model for a transaction."""
    hex: hexstr
    """The transaction hex."""
    txid: uint256
    """The transaction hash."""
    hash: uint256
    """The transaction hash."""
    version: int
    """The transaction version."""
    size: int
    """The transaction size."""
    vsize: int
    """The transaction vsize."""
    weight: int
    """The transaction weight."""
    locktime: int
    """The transaction locktime."""
    vin: List[VIn]
    """A list of VIn."""
    vout: List[VOut]
    """A list of VOut."""
    blockhash: Optional[uint256]
    """The hash of the block containing the transaction."""
    confirmations: Optional[int]
    """The number of confirmations of the transaction."""
    time: Optional[datetime]
    """The transaction time."""
    blocktime: Optional[datetime]
    """The blocktime."""
