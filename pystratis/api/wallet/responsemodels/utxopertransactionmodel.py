from pystratis.api import Model
from pydantic import Field


class UtxoPerTransactionModel(Model):
    """A pydantic model for utxo per transaction."""
    utxo_per_transaction: int = Field(alias='utxoPerTransaction')
    """The utxo per transaction."""
    count: int = Field(alias='Count')
    """The total number of utxos."""
