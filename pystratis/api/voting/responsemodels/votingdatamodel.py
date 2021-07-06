from pystratis.api import Model
from pystratis.core import PubKey
from pystratis.core.types import uint256


class VotingDataModel(Model):
    """A pydantic model representing voting data."""
    key: PubKey
    """The pubkey."""
    hash: uint256
    """The hash voted upon."""
