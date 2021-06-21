from typing import List, Optional
from pydantic import Field, BaseModel


class BlockModel(BaseModel):
    """A BlockModel."""
    hash: str
    confirmations: int
    size: int
    weight: int
    height: int
    version: int
    version_hex: str = Field(alias='versionHex')
    merkleroot: str
    tx: Optional[List[str]]
    time: int
    median_time: int = Field(alias='mediantime')
    nonce: int
    bits: str
    difficulty: float
    chainwork: str
    n_tx: int = Field(alias='nTx')
    previous_blockhash: str = Field(alias='previousblockhash')
    next_blockhash: Optional[str] = Field(alias='nextblockhash')
    signature: Optional[str]
    modifier_v2: Optional[str] = Field(alias='modifierv2')
    flags: Optional[str]
    hashproof: Optional[str]
    blocktrust: Optional[str]
    chaintrust: Optional[str]

    class Config:
        allow_population_by_field_name = True

    def json(self, *args, **kwargs) -> str:
        return super().json(exclude_none=True, by_alias=True)
