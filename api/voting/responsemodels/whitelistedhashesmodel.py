from typing import Optional
from pybitcoin import Model
from pybitcoin.types import uint256


class WhitelistedHashesModel(Model):
    """A WhitelistedHashesModel."""
    hash: Optional[uint256]
