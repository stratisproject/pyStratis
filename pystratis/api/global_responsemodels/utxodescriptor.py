from typing import Optional
from pydantic import Field, conint
from pystratis.api import Model
from pystratis.core.types import Money, uint256


class UtxoDescriptor(Model):
    """A UtxoDescriptor."""
    transaction_id: Optional[uint256] = Field(alias='transactionId')
    index: Optional[conint(ge=0)]
    script_pubkey: Optional[str] = Field(alias='scriptPubKey')
    amount: Money
