from pydantic import Field, conint
from datetime import datetime
from pystratis.core.types import uint256
from pystratis.api import Model


class MaturedBlockInfoModel(Model):
    """A MaturedBlockInfoModel."""
    block_hash: uint256 = Field(alias='blockHash')
    block_height: conint(ge=0) = Field(alias='blockHeight')
    block_time: datetime = Field(alias='blockTime')
