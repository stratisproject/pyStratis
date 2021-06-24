from pybitcoin import Model
from pybitcoin.types import uint256


class SyncRequest(Model):
    """A request model for the wallet/sync endpoint.

    Args:
        hash_id: uint256
    """
    hash_id: uint256
