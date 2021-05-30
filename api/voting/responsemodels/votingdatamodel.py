from pybitcoin import Model
from pybitcoin.types import uint256, hexstr


class VotingDataModel(Model):
    """A VotingDataModel."""
    key: hexstr
    hash: uint256
