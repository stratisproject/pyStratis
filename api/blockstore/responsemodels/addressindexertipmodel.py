from typing import Optional
from pydantic import conint, Field
from pybitcoin import Model
from pybitcoin.types import uint256


class AddressIndexerTipModel(Model):
    """An AddressIndexerTipModel."""
    tip_hash: Optional[uint256] = Field(alias='TipHash')
    tip_height: Optional[conint(ge=0)] = Field(alias='TipHeight')
