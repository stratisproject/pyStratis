from typing import Optional
from pydantic import Field, conint
from pystratis.core import Model


class GetStakingInfoModel(Model):
    """A GetStakingInfoModel."""
    enabled: Optional[bool]
    staking: Optional[bool]
    errors: Optional[str]
    current_blocksize: Optional[conint(ge=0)] = Field(alias='currentBlockSize')
    current_block_tx: Optional[conint(ge=0)] = Field(alias='currentBlockTx')
    pooled_tx: Optional[conint(ge=0)] = Field(alias='pooledTx')
    difficulty: Optional[float]
    search_interval: Optional[conint(ge=0)] = Field(alias='searchInterval')
    weight: Optional[conint(ge=0)]
    net_stake_weight: Optional[conint(ge=0)] = Field(alias='netStakeWeight')
    immature: Optional[conint(ge=0)]
    expected_time: Optional[conint(ge=0)] = Field(alias='expectedTime')
