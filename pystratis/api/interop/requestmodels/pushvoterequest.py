from pydantic import Field
from pystratis.api import Model


class PushVoteRequest(Model):
    """A pydantic model of a pushvote request."""
    request_id: int = Field(alias='requestId')
    """The request id."""
    vote_id: int = Field(alias='voteId')
    """The vote id."""
