from typing import Optional, List
from pydantic import BaseModel, Field, conint


class PollViewModel(BaseModel):
    """A PollViewModel."""
    is_pending: bool = Field(alias='IsPending')
    is_executed: bool = Field(alias='IsExecuted')
    poll_id: int = Field(alias='Id')
    poll_voted_in_favor_blockdata_hash: str = Field(alias='PollVotedInFavorBlockDataHash')
    poll_voted_in_favor_blockdata_height: Optional[conint(ge=0)] = Field(alias='PollVotedInFavorBlockDataHeight')
    poll_start_favor_blockdata_hash: str = Field(alias='PollStartFavorBlockDataHash')
    poll_start_favor_blockdata_height: Optional[conint(ge=0)] = Field(alias='PollStartFavorBlockDataHeight')
    poll_executed_blockdata_hash: str = Field(alias='PollExecutedBlockDataHash')
    poll_executed_blockdata_height: Optional[conint(ge=0)] = Field(alias='PollExecutedBlockDataHeight')
    pubkeys_hex_voted_in_favor: List[str] = Field(alias='PubKeysHexVotedInFavor')
    voting_data_string: str = Field(alias='VotingDataString')

    class Config:
        allow_population_by_field_name = True

    def json(self, *args, **kwargs) -> str:
        return super(PollViewModel, self).json(by_alias=True, exclude_none=True)
