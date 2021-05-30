from pydantic import Field, conint
from pybitcoin import Model


class GetStakingInfoModel(Model):
    """A GetStakingInfoModel."""
    enabled: bool
    staking: bool
    errors: str
    current_blocksize: conint(ge=0) = Field(alias='currentBlockSize')
    current_block_tx: conint(ge=0) = Field(alias='currentBlockTx')
    pooled_tx: conint(ge=0) = Field(alias='pooledTx')
    difficulty: float
    search_interval: conint(ge=0) = Field(alias='searchInterval')
    weight: conint(ge=0)
    net_stake_weight: conint(ge=0) = Field(alias='netStakeWeight')
    immature: conint(ge=0)
    expected_time: conint(ge=0) = Field(alias='expectedTime')
