from pydantic import Field, validator
from pybitcoin import Model


class ExecutedPollsRequest(Model):
    """An ExecutedPollsRequest."""
    vote_type: str = Field(alias='voteType')
    pubkey_of_member_being_voted_on: str = Field(alias='pubKeyOfMemberBeingVotedOn')

    # noinspection PyMethodParameters,PyUnusedLocal
    @validator('vote_type')
    def validate_vote_type(cls, v, values):
        allowed_methods = [
            'KickFederationMember',
            'AddFederationMember',
            'WhitelistHash',
            'RemoveHash'
        ]
        if v not in allowed_methods:
            raise ValueError(f'Invalid voteType. Must be: {allowed_methods}')
        return v

