from pydantic import Field
from pystratis.api import Model
from pystratis.core.types import uint256


# noinspection PyUnresolvedReferences
class SyncRequest(Model):
    """A request model for the federationwallet/sync endpoint.

    Args:
        block_hash (uint256): The block hash at which to start sync.
    """
    block_hash: uint256 = Field(alias='hash')
