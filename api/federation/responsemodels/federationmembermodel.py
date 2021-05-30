from typing import Optional
from pybitcoin import Model
from pybitcoin.types import Money, hexstr
from pydantic import Field


class FederationMemberModel(Model):
    """A FederationMemberModel."""
    pubkey: hexstr
    collateral_amount: Money = Field(alias='collateralAmount')
    last_active_time: Optional[str] = Field(alias='lastActiveTime')
    period_of_inactivity: Optional[str] = Field(alias='periodOfInactivity')
