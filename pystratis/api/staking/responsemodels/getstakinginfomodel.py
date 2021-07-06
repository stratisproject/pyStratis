from typing import Optional
from pydantic import Field
from pystratis.api import Model


class GetStakingInfoModel(Model):
    """A pydantic model for staking information."""
    enabled: bool
    """If true, staking is enabled."""
    staking: bool
    """If true, is currently staking."""
    errors: Optional[str]
    """Error messages, if present."""
    current_blocksize: int = Field(alias='currentBlockSize')
    """The current block size."""
    current_block_tx: int = Field(alias='currentBlockTx')
    """The current number of block transactions."""
    pooled_tx: int = Field(alias='pooledTx')
    """The number of pooled transactions."""
    difficulty: float
    """The current difficulty."""
    search_interval: int = Field(alias='searchInterval')
    """The search interval."""
    weight: int
    """The current staking weight."""
    net_stake_weight: Optional[int] = Field(alias='netStakeWeight')
    """The network staking weight."""
    immature: int
    """The number of immature coins that can't stake."""
    expected_time: int = Field(alias='expectedTime')
    """The expected number of seconds between stakes."""
