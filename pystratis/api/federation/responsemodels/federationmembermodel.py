from typing import Optional
from pystratis.api import Model
from pystratis.core import PubKey
from pystratis.core.types import Money
from pydantic import Field


class FederationMemberModel(Model):
    """A FederationMemberModel."""
    pubkey: PubKey
    collateral_amount: Optional[Money] = Field(alias='collateralAmount')
    last_active_time: Optional[str] = Field(alias='lastActiveTime')
    period_of_inactivity: Optional[str] = Field(alias='periodOfInactivity')
