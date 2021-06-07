from typing import Optional
from pydantic import Field, conint
from pybitcoin.types import Money
from .federationmembermodel import FederationMemberModel


class FederationMemberDetailedModel(FederationMemberModel):
    """A FederationMemberDetailedModel."""
    poll_start_block_height: Optional[conint(ge=0)] = Field(alias='pollStartBlockHeight')
    poll_number_of_votes_acquired: Optional[conint(ge=0)] = Field(alias='pollNumberOfVotesAcquired')
    poll_finished_block_height: Optional[conint(ge=0)] = Field(alias='pollFinishedBlockHeight')
    poll_will_finish_in_blocks: Optional[conint(ge=0)] = Field(alias='pollWillFinishInBlocks')
    poll_executed_block_height: Optional[conint(ge=0)] = Field(alias='pollExecutedBlockHeight')
    member_will_start_mining_at_block_height: Optional[conint(ge=0)] = Field(alias='memberWillStartMiningAtBlockHeight')
    member_will_start_earning_rewards_estimate_height: Optional[conint(ge=0)] = Field(alias='memberWillStartEarningRewardsEstimateHeight')
    poll_type: Optional[str] = Field(alias='pollType')
    reward_estimate_per_block: Optional[Money] = Field(alias='rewardEstimatePerBlock')
