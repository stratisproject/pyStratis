from pydantic import Field
from pybitcoin import Address, Model, PubKey
from pybitcoin.types import Money


class ScheduleVoteKickFedMemberRequest(Model):
    """A ScheduleVoteKickFedMemberRequest."""
    pubkey_hex: PubKey = Field(alias='pubKeyHex')
    collateral_amount_satoshis: Money = Field(alias='collateralAmountSatoshis')
    collateral_mainchain_address: Address = Field(alias='collateralMainchainAddress')
