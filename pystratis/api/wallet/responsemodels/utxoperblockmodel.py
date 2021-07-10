from pystratis.api import Model
from pydantic import Field


class UtxoPerBlockModel(Model):
    """A pydantic model representing utxo per block."""
    utxo_per_block: int = Field(alias='utxoPerBlock')
    """The number of utxo per block."""
    count: int = Field(alias='Count')
    """The number of utxos."""

