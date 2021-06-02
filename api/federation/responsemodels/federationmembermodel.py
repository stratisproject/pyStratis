from typing import Optional
from pybitcoin import Model, PubKey
from pybitcoin.types import Money
from pydantic import Field


class FederationMemberModel(Model):
    """A FederationMemberModel."""
    pubkey: PubKey
    collateral_amount: Money = Field(alias='collateralAmount')
    last_active_time: Optional[str] = Field(alias='lastActiveTime')
    period_of_inactivity: Optional[str] = Field(alias='periodOfInactivity')
