from pybitcoin import Model, ScriptPubKey
from pybitcoin.types import Money, uint256
from pydantic import Field, conint


class GetTxOutModel(Model):
    """A GetTxOutModel."""
    best_block: uint256
    confirmations: conint(ge=0)
    value: Money
    script_pubkey: ScriptPubKey = Field(alias='scriptPubKey')
    coinbase: bool
