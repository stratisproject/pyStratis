from pydantic import Field
from pybitcoin import Model
from pybitcoin.types import uint256


class ScheduleVoteRemoveHashRequest(Model):
    """A request model for the voting/schedulevote-removehash endpoint.

    Args:
        hash_id (uint256): The hash to remove.
    """
    hash_id: uint256 = Field(alias='hash')
