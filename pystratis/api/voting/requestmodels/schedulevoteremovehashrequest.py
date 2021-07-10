from pydantic import Field
from pystratis.api import Model
from pystratis.core.types import uint256


# noinspection PyUnresolvedReferences
class ScheduleVoteRemoveHashRequest(Model):
    """A request model for the voting/schedulevote-removehash endpoint.

    Args:
        hash_id (uint256): The hash to remove.
    """
    hash_id: uint256 = Field(alias='hash')
