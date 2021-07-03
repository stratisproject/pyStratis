from pydantic import Field
from pystratis.api import Model
from pystratis.core.types import uint256


class ScheduleVoteWhitelistHashRequest(Model):
    """A request model for the voting/schedulevote-whitelist endpoint.

    Args:
        hash_id (uint256): The hash to whitelist.
    """
    hash_id: uint256 = Field(alias='hash')
