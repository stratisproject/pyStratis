from pydantic import Field
from pystratis.api import Model
from pystratis.core.types import Money, uint256


class UTXOModel(Model):
    """A pydantic model representing a unspent transaction output (utxo)."""
    transaction_id: uint256 = Field(alias='txId')
    """The transaction hash of the transaction containing the utxo."""
    index: int
    """The output index of the utxo."""
    script_pubkey: str = Field(alias='scriptPubKey')
    """The scriptpubkey of the utxo."""
    value: Money
    """The value of the utxo in coin units."""
