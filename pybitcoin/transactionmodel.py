from typing import Optional, List
from datetime import datetime
from pydantic import BaseModel, conint
from pybitcoin.types import uint256, hexstr
from .vin import VIn
from .vout import VOut


class TransactionModel(BaseModel):
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

    class Config:
        allow_population_by_field_name = True

    def json(self, *args, **kwargs) -> str:
        return super().json(exclude_none=True, by_alias=True)
