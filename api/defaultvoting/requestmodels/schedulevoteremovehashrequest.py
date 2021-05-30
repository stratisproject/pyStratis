from pybitcoin import Model
from pybitcoin.types import uint256


class ScheduleVoteRemoveHashRequest(Model):
    """A ScheduleVoteRemoveHashRequest."""
    hash: uint256
