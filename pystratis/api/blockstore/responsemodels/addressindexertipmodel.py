from pydantic import Field
from pystratis.api import Model
from pystratis.core.types import uint256


class AddressIndexerTipModel(Model):
    """A pydantic model for the address indexer tip."""
    tip_hash: uint256 = Field(alias='tipHash')
    """The block hash of the block at the address indexer tip."""
    tip_height: int = Field(alias='tipHeight')
    """The block height of the address indexer tip."""
