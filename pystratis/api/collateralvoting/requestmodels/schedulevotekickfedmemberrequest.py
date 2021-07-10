from pydantic import Field, conint
from pystratis.api import Model
from pystratis.core import PubKey
from pystratis.core.types import Address


# noinspection PyUnresolvedReferences
class ScheduleVoteKickFedMemberRequest(Model):
    """A request model for collateralvoting/schedulevote-kickfedmember endpoint.

    Args:
        pubkey_hex (PubKey): The fedmember pubkey hex value.
        collateral_amount_satoshis (conint(ge=0)): The collateral amount in satoshis.
        collateral_mainchain_address (Address): The mainchain address holding the collateral.
    """
    pubkey_hex: PubKey = Field(alias='pubKeyHex')
    collateral_amount_satoshis: conint(ge=0) = Field(alias='collateralAmountSatoshis')
    collateral_mainchain_address: Address = Field(alias='collateralMainchainAddress')
