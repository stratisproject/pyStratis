from typing import Optional
from pybitcoin import Model, ScriptPubKey
from pybitcoin.types import Money, uint256
from pydantic import Field, conint


class GetTxOutModel(Model):
    """A GetTxOutModel."""
    best_block: Optional[uint256] = Field(alias='bestblock')
    confirmations: Optional[conint(ge=0)]
    value: Optional[Money]
    script_pubkey: Optional[ScriptPubKey] = Field(alias='scriptPubKey')
    coinbase: Optional[bool]
