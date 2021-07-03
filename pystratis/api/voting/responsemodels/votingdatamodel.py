from typing import Optional
from pystratis.api import Model
from pystratis.core import PubKey
from pystratis.core.types import uint256


class VotingDataModel(Model):
    """A VotingDataModel."""
    key: Optional[PubKey]
    hash: Optional[uint256]
