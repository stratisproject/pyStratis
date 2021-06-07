from typing import Optional
from pybitcoin import Model, PubKey
from pybitcoin.types import uint256


class VotingDataModel(Model):
    """A VotingDataModel."""
    key: Optional[PubKey]
    hash: Optional[uint256]
