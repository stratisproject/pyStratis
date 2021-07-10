from pydantic import Field
from pystratis.api import Model
from pystratis.core.types import uint256


# noinspection PyUnresolvedReferences
class SyncRequest(Model):
    """A request_model for the notifications/sync endpoint.

    Args:
        sync_from (uint256): The block hash to start syncing at.
    """
    sync_from: uint256 = Field(alias='from')
