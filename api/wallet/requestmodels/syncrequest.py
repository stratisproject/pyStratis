from pybitcoin import Model
from pybitcoin.types import uint256


class SyncRequest(Model):
    """A SyncRequest."""
    hash: uint256
