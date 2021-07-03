from typing import Optional
from pydantic import conint, Field
from pystratis.core import Model
from pystratis.core.types import uint256


class AddressIndexerTipModel(Model):
    """An AddressIndexerTipModel."""
    tip_hash: Optional[uint256] = Field(alias='tipHash')
    tip_height: Optional[conint(ge=0)] = Field(alias='tipHeight')
