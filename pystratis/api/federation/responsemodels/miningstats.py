from pydantic import Field
from pystratis.api import Model
from pystratis.core.types import Address


class MiningStats(Model):
    """A pydantic model for mining stats."""
    miner_hits: int = Field(alias='minerHits')
    """The number of miner hits in the last round."""
    mining_address: Address = Field(alias="miningAddress")
    """The mining address."""
    produced_block_in_last_round: bool = Field(alias='producedBlockInLastRound')
    """If the miner produced a block in the last round."""
