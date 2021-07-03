from typing import Optional
from pydantic import Field, conint
from pystratis.api import Model
from pystratis.core.types import uint256, hexstr


class BlockHeaderModel(Model):
    """A BlockHeaderModel."""
    version: Optional[conint(ge=0)]
    merkleroot: Optional[hexstr]
    nonce: Optional[conint(ge=0)]
    bits: Optional[str]
    previous_blockhash: Optional[uint256] = Field(alias='previousblockhash')
    time: Optional[conint(ge=0)]
