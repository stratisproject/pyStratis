from pydantic import Field
from pybitcoin import Model
from pybitcoin.types import uint256


class SyncRequest(Model):
    """A SyncRequest."""
    sync_from: uint256 = Field(alias='from')
