from pydantic import Field
from pystratis.api import Model
from pystratis.core.types import Money, uint256


class UTXOModel(Model):
    """A pydantic model for a utxo."""
    tx_hash: uint256 = Field(alias='hash')
    """The tx hash"""
    n: int
    """The outpoint index."""
    amount: Money = Field(alias='satoshis')
    """The amount in Money units"""
