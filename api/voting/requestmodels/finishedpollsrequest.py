from pydantic import Field, conint
from pybitcoin import Model, PubKey


class FinishedPollsRequest(Model):
    """A FinishedPollsRequest."""
    vote_type: conint(ge=0, le=3) = Field(alias='voteType')
    pubkey_of_member_being_voted_on: PubKey = Field(alias='pubKeyOfMemberBeingVotedOn')
