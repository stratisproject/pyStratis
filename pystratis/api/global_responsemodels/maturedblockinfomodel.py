from pydantic import Field
from datetime import datetime
from pystratis.core.types import uint256
from pystratis.api import Model


class MaturedBlockInfoModel(Model):
    """A pydantic model representing a married block."""
    block_hash: uint256 = Field(alias='blockHash')
    """The block hash."""
    block_height: int = Field(alias='blockHeight')
    """The block height."""
    block_time: datetime = Field(alias='blockTime')
    """The time block was produced."""
