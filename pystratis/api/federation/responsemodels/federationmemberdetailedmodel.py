from typing import Optional
from pydantic import Field
from pystratis.core.types import Money
from .federationmembermodel import FederationMemberModel


class FederationMemberDetailedModel(FederationMemberModel):
    """A pydantic model for details on federation members."""
    poll_start_block_height: Optional[int] = Field(alias='pollStartBlockHeight')
    """The poll start block height."""
    poll_number_of_votes_acquired: Optional[int] = Field(alias='pollNumberOfVotesAcquired')
    """The number of poll votes acquired."""
    poll_finished_block_height: Optional[int] = Field(alias='pollFinishedBlockHeight')
    """The poll finished block height."""
    poll_will_finish_in_blocks: Optional[int] = Field(alias='pollWillFinishInBlocks')
    """The number of blocks until the poll finishes."""
    poll_executed_block_height: Optional[int] = Field(alias='pollExecutedBlockHeight')
    """The block heigh where poll was executed, if it has occurred."""
    member_will_start_mining_at_block_height: Optional[int] = Field(alias='memberWillStartMiningAtBlockHeight')
    """Height when the member will start mining."""
    member_will_start_earning_rewards_estimate_height: Optional[int] = Field(alias='memberWillStartEarningRewardsEstimateHeight')
    """Height when member will start earning rewards."""
    poll_type: Optional[str] = Field(alias='pollType')
    """The poll type."""
    reward_estimate_per_block: Optional[Money] = Field(alias='rewardEstimatePerBlock')
    """The reward estimate per block."""
