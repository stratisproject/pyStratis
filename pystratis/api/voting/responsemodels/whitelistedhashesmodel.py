from pystratis.api import Model
from pystratis.core.types import uint256


class WhitelistedHashesModel(Model):
    """A pydantic model for a whitelisted hash."""
    hash: uint256
    """A whitelisted hash."""
