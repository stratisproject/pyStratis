from typing import List, Optional
from pydantic import Field, conint
from pystratis.core import Model, PubKey
from pystratis.core.types import Address


class FederationGatewayInfoModel(Model):
    """A FederationGatewayInfoModel."""
    active: Optional[bool]
    mainchain: Optional[bool]
    endpoints: Optional[List[str]]
    multisig_pubkey: Optional[PubKey] = Field(alias='multisigPubKey')
    federation_multisig_pubkeys: Optional[List[PubKey]] = Field(alias='federationMultisigPubKeys')
    mining_pubkey: Optional[PubKey] = Field(default='', alias='miningPubKey')
    federation_mining_pubkeys: Optional[List[PubKey]] = Field(default=[], alias='federationMiningPubKeys')
    multisig_address: Optional[Address] = Field(alias='multisigAddress')
    multisig_redeem_script: Optional[str] = Field(alias='multisigRedeemScript')
    multisig_redeem_script_payment_script: Optional[str] = Field(alias='multisigRedeemScriptPaymentScript')
    min_conf_small_deposits: Optional[conint(ge=0)] = Field(alias='minconfsmalldeposits')
    min_conf_normal_deposits: Optional[conint(ge=0)] = Field(alias='minconfnormaldeposits')
    min_conf_large_deposits: Optional[conint(ge=0)] = Field(alias='minconflargedeposits')
    min_conf_distribution_deposits: Optional[conint(ge=0)] = Field(alias='minconfdistributiondeposits')
