from typing import Optional, List
from pydantic import Field
from pystratis.core import PubKey
from pystratis.core.types import uint256
from pystratis.api import Model


class PollViewModel(Model):
    """A pydantic model for polling data."""
    is_pending: bool = Field(alias='IsPending')
    """If true, poll is pending."""
    is_executed: bool = Field(alias='IsExecuted')
    """If true, poll has been executed."""
    poll_id: int = Field(alias='Id')
    """The poll id."""
    poll_voted_in_favor_blockdata_hash: Optional[uint256] = Field(alias='PollVotedInFavorBlockDataHash')
    """If voted in favor, the block of the vote."""
    poll_voted_in_favor_blockdata_height: Optional[int] = Field(alias='PollVotedInFavorBlockDataHeight')
    """If voted in favor, the height of the block."""
    poll_start_favor_blockdata_hash: Optional[uint256] = Field(alias='PollStartFavorBlockDataHash')
    """The block hash when polling started."""
    poll_start_favor_blockdata_height: Optional[int] = Field(alias='PollStartFavorBlockDataHeight')
    """The block height when polling started."""
    poll_executed_blockdata_hash: Optional[uint256] = Field(alias='PollExecutedBlockDataHash')
    """The block hash when poll was executed, if executed."""
    poll_executed_blockdata_height: Optional[int] = Field(alias='PollExecutedBlockDataHeight')
    """The block height when poll was executed, if executed."""
    pubkeys_hex_voted_in_favor: List[PubKey] = Field(alias='PubKeysHexVotedInFavor')
    """A list of pubkeys voting in favor of poll."""
    voting_data_string: str = Field(alias='VotingDataString')
    """Voting data."""
