from typing import Optional
from pydantic import Field
from pybitcoin import Model
from pybitcoin.types import uint256


class GetBlockHeaderRequest(Model):
    """A GetBlockHeaderRequest."""
    block_hash: uint256
    is_json_format: Optional[bool] = Field(default=True, alias='isJsonFormat')
