from typing import Optional
from pystratis.core import Model, PubKey
from pystratis.core.types import uint256


class VotingDataModel(Model):
    """A VotingDataModel."""
    key: Optional[PubKey]
    hash: Optional[uint256]
