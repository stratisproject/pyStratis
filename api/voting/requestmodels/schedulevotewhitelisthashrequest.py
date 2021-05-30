from pybitcoin import Model
from pybitcoin.types import uint256


class ScheduleVoteWhitelistHashRequest(Model):
    """A ScheduleVoteWhitelistHashRequest."""
    hash: uint256
