from pydantic import Field
from pystratis.api import Model
from pystratis.core.types import uint256


# noinspection PyUnresolvedReferences
class SyncRequest(Model):
    """A request model for the wallet/sync endpoint.

    Args:
        block_hash (uint256): The hash to start syncing from.
    """
    block_hash: uint256 = Field(alias='hash')
