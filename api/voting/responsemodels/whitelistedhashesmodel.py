from pybitcoin import Model
from pybitcoin.types import uint256


class WhitelistedHashesModel(Model):
    """A WhitelistedHashesModel."""
    hash: uint256
