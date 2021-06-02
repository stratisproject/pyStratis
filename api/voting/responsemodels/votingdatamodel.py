from pybitcoin import Model, PubKey
from pybitcoin.types import uint256


class VotingDataModel(Model):
    """A VotingDataModel."""
    key: PubKey
    hash: uint256
