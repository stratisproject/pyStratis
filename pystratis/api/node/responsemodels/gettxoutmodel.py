from pystratis.api import Model
from pystratis.api.global_responsemodels import ScriptPubKey
from pystratis.core.types import Money, uint256
from pydantic import Field


class GetTxOutModel(Model):
    """A pydantic model for get tx out response."""
    best_block: uint256 = Field(alias='bestblock')
    """The highest block where utxo was present."""
    confirmations: int
    """The numberof confirmations."""
    value: Money
    """The value of the utxo."""
    script_pubkey: ScriptPubKey = Field(alias='scriptPubKey')
    """The utxo scriptpubkey."""
    coinbase: bool
    """If true, the utxo originated as a coinbase transaction."""
