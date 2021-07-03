from typing import Optional
from pydantic import Field, conint
from pystratis.api import Model
from pystratis.core.types import Money, uint256


class UTXOModel(Model):
    """A UTXOModel."""
    transaction_id: Optional[uint256] = Field(alias='txId')
    index: Optional[conint(ge=0)]
    script_pubkey: Optional[str] = Field(alias='scriptPubKey')
    value: Optional[Money]
