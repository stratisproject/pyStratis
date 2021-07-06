from pystratis.api import Model
from pystratis.core import PubKey
from pystratis.core.types import Money
from pydantic import Field


class FederationMemberModel(Model):
    """A pydantic model for a federation member."""
    pubkey: PubKey
    """The federation member's pubkey."""
    collateral_amount: Money = Field(alias='collateralAmount')
    """The federation member's collateral amount."""
    last_active_time: str = Field(alias='lastActiveTime')
    """The federation member's last active time."""
    period_of_inactivity: str = Field(alias='periodOfInactivity')
    """The federation member's period of inactivity."""
