from pydantic import Field
from pystratis.api import Model
from pystratis.core.types import hexstr


# noinspection PyUnresolvedReferences
class ScheduleVoteKickMemberRequest(Model):
    """A request model for the voting/schedulevote-kickmember endpoint.

    Args:
        pubkey (hexstr): The pubkey to vote on kicking.
    """
    pubkey: hexstr
