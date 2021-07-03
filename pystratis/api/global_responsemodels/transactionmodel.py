from typing import Optional, List
from datetime import datetime
from pydantic import conint
from pystratis.core.types import uint256, hexstr
from pystratis.api import Model
from .vin import VIn
from .vout import VOut


class TransactionModel(Model):
    """A TransactionModel."""
    hex: Optional[hexstr]
    txid: Optional[uint256]
    hash: Optional[uint256]
    version: Optional[conint(ge=0)]
    size: Optional[conint(ge=0)]
    vsize: Optional[conint(ge=0)]
    weight: Optional[conint(ge=0)]
    locktime: Optional[conint(ge=0)]
    vin: Optional[List[VIn]]
    vout: Optional[List[VOut]]
    blockhash: Optional[uint256]
    confirmations: Optional[int]
    time: Optional[datetime]
    blocktime: Optional[datetime]
